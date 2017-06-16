#coding=utf-8  
""" 
本应用主要功能 
1.用户选择喜欢的标签加关注 
2.获取用户粉丝中自己还没有关注的,->加关注,提高粉丝稳定性 
3.获取用户关注列表中没有回粉的,并可以一键取消关注 
2,3两个功能基本实现,有一缺点,数据量一大,很慢很慢 
1功能不太好,主要是通过一个线程去搜索数据,把感兴趣的用户放入数据库,当用户选择加关注标签时,从数据库中取数据, 
以前用sqlite3比较少,一用发现还是有好多值得研究的地方,主要是线程安全....,慢慢研究.... 
"""  
  
import os  
import sys  
import key  
import web  
import threading  
import sqlite3  
import time  
from weibopy.auth import OAuthHandler  
from weibopy.api import API  
from jinja2 import Environment,FileSystemLoader  
  
""" 
url配置 
"""  
urls = (  
     '/', 'Login',  
     '/index','Index',  
     '/callback','CallBack',  
     '/logout','LogOut',  
     '/(.*)/', 'Redirect',  
     '/tag', 'Tag',  
     '/noattention','Noattention',  
     '/fensiattention','Fensiattention',  
     '/minusattention','Minusattention',  
     '/delattention','Delattention'  
 )  
  
app=web.application(urls,globals())  
  
if web.config.get('_session') is None:  
     session = web.session.Session(app,web.session.DiskStore("sina"))  
     web.config._session = session  
else:  
     session = web.config._session  
  
""" 
   用jinja2模板渲染文件 
"""  
def render_template(template_name,**context):  
     extensions=context.pop('extensions',[])  
     globals=context.pop("globals",{})  
     jinja_env=Environment(  
         loader=FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')),  
         extensions=extensions)  
     jinja_env.globals.update(globals)  
     return jinja_env.get_template(template_name).render(context)  
  
  
""" 
定义404请求页面 
"""  
def notfound():  
     info="亲,您所请求的页面不存在,系统在3秒后自动返回..."  
     return web.notfound(render_template('error.html',info=info.decode('utf-8')))  
  
db=web.database(dbn='sqlite',db='tag.s3db')  
  
""" 
要求tag 
"""  
tagdict={'水瓶座':1,'双鱼座':2,'白羊座':3,'金牛座':4,'双子座':5,'巨蟹座':6,'狮子座':7,'处女座':8,'天秤座':9,'天蝎座':10,'射手座':11,  
         '摩羯座':12,'吃':13,'听歌':14,'淘宝':15,'网购':16,'数码':17,'摄影':18,'睡觉':19,'旅游':20,'体育':21,'动漫':22,'游戏':23,  
         '股票':24,'交友':25,'宅女':26,'宅男':27,'时尚':28,'浪漫':29,'美女':30,'创业':31,'IT':32,'媒体':33,'营销':34}  
systag=['水瓶座','双鱼座','白羊座','金牛座','双子座','巨蟹座','狮子座','处女座','天秤座','天蝎座','射手座','摩羯座','吃','听歌','淘宝',  
        '网购','数码','摄影','睡觉','旅游','体育','动漫','游戏','股票','交友','宅女','宅男','时尚','浪漫','美女','创业','IT','媒体','营销']  
  
conn=sqlite3.connect('tag.s3db',check_same_thread=False) #允许其它线程使用这个连接  
conn.text_factory = str  
cursor=conn.cursor()  
  
class Setag(threading.Thread):  
    """ 
这个线程主要是用来搜索用户tag,如果满足tag要求就写入数据库中, 
    """  
    def authorization(self):  
        """ 
        开发者认证 
        """  
        auth = OAuthHandler(key.CONSUME_KEY, key.CONSUME_SECRET)  
        auth.setToken(key.TOKEN,key.TOKEN_SECRET)  
        self.api = API(auth)  
        self.cursor=cursor  
  
    def adduser(self,uid):  
        """ 
        遍历uid用户的tag,满足条件加入数据库 
        """  
        try:  
            fan=self.api.followers_ids(uid)  
            fanuid=fan.ids  
            for id in fanuid:  
                tags=self.api.tags(id)  
                tt=[]  
                for t in tags:  
                    tagid=t.__getattribute__('id')  
                    value=t.__getattribute__(tagid)  
                    tt.append(value.encode('utf-8'))  
                """ 
                获取用户tag与要求标签的交集 
                """  
                common=set(tt).intersection(set(systag))  
                if len(common)==0:  
                    continue  
                else:  
                    for t in common:  
                        """ 
                        获取tag对应的tagid 
                        """  
                        tagindex=tagdict[t]  
                        try:  
                            self.cursor.execute("insert into taginfo(uid,tagid) values(%d,%d)" %(int(id),int(tagindex)))  
                            conn.commit()  
                        except:  
                            continue  
        except:  
            time.sleep(120)  
            pass  
        finally:  
            time.sleep(60)  
            """ 
            将uid用户的第一个粉丝uid传给adduser 
            """  
            return self.adduser(fanuid[0])  
  
    def run(self):  
        self.authorization()  
        me=self.api.verify_credentials()  
        """ 
        将我自己的uid给adduser 
        """  
        self.adduser(me.id)  
  
""" 
定义404请求页面 
"""  
app.notfound= notfound  
 #首页  
 #首先从session中获取access_token，没有就转向新浪微博页面认证  
 #认证成功后将access_token保存在session中  
""" 
首页是登陆页面,通过新浪微博授权 
"""  
class Login:  
    def GET(self):  
        return render_template('login.html')  
  
""" 
新浪微博授权原理: 
首先首页判断有无用户session信息,如果有则跳转到相应地址, 
没有则引导用户跳转到授权uri,授权后自动跳转到永远自定义的回调地址, 
回调地址保存用户session信息,跳转到首页,这时已有用户session信息,干坏事吧.... 
"""  
class Index:  
     def GET(self):  
         access_token=session.get('access_token',None)  
         if not access_token:  
             """ 
             key.py中放置了开发者的信息 
             """  
             auth = OAuthHandler(key.CONSUME_KEY, key.CONSUME_SECRET,web.ctx.get('homedomain')+'/callback')  
             #获取授权url  
             auth_url = auth.get_authorization_url()  
             session.request_token=auth.request_token  
             web.seeother(auth_url)  
         else:  
             auth = OAuthHandler(key.CONSUME_KEY, key.CONSUME_SECRET)  
             auth.access_token=access_token  
             api=API(auth)  
             user=api.verify_credentials()  
             return render_template('index.html',user=user)  
  
  
""" 
 页面回调，新浪微博验证成功后会返回本页面 
"""  
class CallBack:  
     def GET(self):  
         try:  
             ins=web.input()  
             oauth_verifier=ins.get('oauth_verifier',None)  
             request_token=session.get('request_token',None)  
             auth=OAuthHandler(key.CONSUME_KEY, key.CONSUME_SECRET)  
             auth.request_token=request_token  
             access_token=auth.get_access_token(oauth_verifier)  
             session.access_token=access_token  
             web.seeother("/index")  
         except Exception:  
             info="亲,系统繁忙,请稍后再试......,系统在3秒后自动返回..."  
             return render_template('error.html',info=info.decode('utf-8'))  
  
""" 
重定向用户输入uri后的/ 
"""  
class Redirect:  
    def GET(self,path):  
        web.seeother('/'+path)  
  
class Tag:  
    """ 
    获取用户选择加关注的tag 
    """  
    def GET(self):  
        data=web.input()  
        try:  
            select=data.star  
        except:  
            try:  
                select=data.hobby  
            except:  
                try:  
                    select=data.personality  
                except:  
                    select=data.job  
        try:  
            auth = OAuthHandler(key.CONSUME_KEY, key.CONSUME_SECRET)  
            auth.access_token=session['access_token']  
            api=API(auth)  
            seuid=[]  
            nu=0  
            """ 
            这里写的很不好..... 
            """  
            while True:  
                re=cursor.execute('select uid from taginfo where tagid=%d limit 20' %select).fetchall()  
                for r in re:  
                    seuid.append(r[0])  
                for s in seuid:  
                    try:  
                        api.create_friendship(user_id=s)  
                        nu+=1  
                    except:  
                        continue  
                if nu>=50:  
                    break  
  
            info="恭喜您已成功关注%d位用户....." %nu  
            return render_template('success.html',info=info.decode('utf-8'))  
        except:  
            info="亲,系统繁忙,请稍后再试......,系统在3秒后自动返回..."  
            return render_template('error.html',info=info.decode('utf-8'))  
  
class Noattention:  
    """ 
    获取我的粉丝中我没有加关注的,把数据传给noattention.html页面显示... 
    """  
    def GET(self):  
        try:  
            auth=OAuthHandler(key.CONSUME_KEY,key.CONSUME_SECRET)  
            auth.access_token=session['access_token']  
            api=API(auth)  
            user=api.verify_credentials()  
            fan=[]  
            next_cursor=-1  
            while next_cursor!=0:  
                timeline=api.followers(user.id,'','','',next_cursor)  
                if isinstance(timeline,tuple):  
                    next_cursor=timeline[1]  
                    for line in timeline[0]:  
                        fid=line.__getattribute__("id")  
                        fname=line.__getattribute__("screen_name")  
                        fan.append((fid,fname))  
  
                else:  
                    next_cursor=0  
                    for line in timeline:  
                        fid=line.__getattribute__("id")  
                        fname=line.__getattribute__("screen_name")  
                        fan.append((fid,fname))  
  
            friend=[]  
            next_cursor=-1  
            while next_cursor!=0:  
                timeline=api.friends(user.id,'','','',next_cursor)  
                if isinstance(timeline,tuple):  
                    next_cursor=timeline[1]  
                    for line in timeline[0]:  
                        frid=line.__getattribute__("id")  
                        frname=line.__getattribute__("screen_name")  
                        friend.append((frid,frname))  
                else:  
                    next_cursor=0  
                    for line in timeline:  
                        frid=line.__getattribute__("id")  
                        frname=line.__getattribute__("screen_name")  
                        friend.append((frid,frname))  
            #获取我的粉丝中还不是我的关注对象  
            fanNotAttention=list(set(fan).difference(set(friend)))  
            nu=len(fanNotAttention)  
            if nu==0:  
                return render_template('noattentionok.html',nu=nu)  
            else:  
                return render_template('noattention.html',nu=nu,fanNotAttention=fanNotAttention)  
  
        except:  
            info="亲,系统繁忙,请稍后再试......,系统在3秒后自动返回..."  
            return render_template('error.html',info=info.decode('utf-8'))  
  
class Fensiattention:  
    """ 
    对未加关注的粉丝加关注 
    """  
    def GET(self):  
        #获取noattentionok.html传过来的数据  
        data=web.input()  
        on=[]  
        try:  
            auth=OAuthHandler(key.CONSUME_KEY,key.CONSUME_SECRET)  
            auth.access_token=session['access_token']  
            api=API(auth)  
            """ 
            获取noattention.html页面传过来的uid,通过checkbox,由于有一个全选按钮,如果点击,则去掉 
            """  
            for x in data:  
                on.append(x)  
            try:  
                on.remove('checkbox2')  
            except:  
                pass  
            nu=len(on)  
            if nu==0:  
                pass  
            if nu>60:  
                on=on[:60]  
                nu=60  
            """ 
            一次最多加60次关注 
            """  
            map(api.create_friendship,on)  
            info="恭喜您已成功关注%d位用户....." %nu  
            return render_template('success.html',info=info.decode('utf-8'))  
        except:  
             info="亲,系统繁忙,请稍后再试......,系统在3秒后自动返回..."  
             return render_template('error.html',info=info.decode('utf-8'))  
  
  
class Minusattention:  
    """ 
    获取我的关注中不是我粉丝的,即不回粉的家伙,把数据传给attentionnotfan.html显示... 
    """  
    def GET(self):  
        try:  
            auth=OAuthHandler(key.CONSUME_KEY,key.CONSUME_SECRET)  
            auth.access_token=session['access_token']  
            api=API(auth)  
            user=api.verify_credentials()  
            fan=[]  
            next_cursor=-1  
            while next_cursor!=0:  
                timeline=api.followers(user.id,'','','',next_cursor)  
                if isinstance(timeline,tuple):  
                    next_cursor=timeline[1]  
                    for line in timeline[0]:  
                        fid=line.__getattribute__("id")  
                        fname=line.__getattribute__("screen_name")  
                        fan.append((fid,fname))  
  
                else:  
                    next_cursor=0  
                    for line in timeline:  
                        fid=line.__getattribute__("id")  
                        fname=line.__getattribute__("screen_name")  
                        fan.append((fid,fname))  
  
            friend=[]  
            next_cursor=-1  
            while next_cursor!=0:  
                timeline=api.friends(user.id,'','','',next_cursor)  
                if isinstance(timeline,tuple):  
                    next_cursor=timeline[1]  
                    for line in timeline[0]:  
                        frid=line.__getattribute__("id")  
                        frname=line.__getattribute__("screen_name")  
                        friend.append((frid,frname))  
                else:  
                    next_cursor=0  
                    for line in timeline:  
                        frid=line.__getattribute__("id")  
                        frname=line.__getattribute__("screen_name")  
                        friend.append((frid,frname))  
            attentionNotFan=list(set(friend).difference(set(fan)))  
            nu=len(attentionNotFan)  
            if nu==0:  
                return render_template('attentionnotfanok.html',nu=nu)  
            else:  
                return render_template('attentionnotfan.html',nu=nu,attentionNotFan=attentionNotFan)  
  
        except:  
             info="亲,系统繁忙,请稍后再试......,系统在3秒后自动返回..."  
             return render_template('error.html',info=info.decode('utf-8'))  
  
  
class Delattention:  
    """ 
    获取attentionnotfan.html页面选择的用户,并一键取消关注 
    """  
    def GET(self):  
        #获取attentionnotfan.html传过来的数据  
        data=web.input()  
        on=[]  
        try:  
            auth=OAuthHandler(key.CONSUME_KEY,key.CONSUME_SECRET)  
            auth.access_token=session['access_token']  
            api=API(auth)  
            for x in data:  
                on.append(x)  
            try:  
                #同理,由于有全选按钮.....  
                on.remove('checkbox2')  
            except:  
                pass  
            nu=len(on)  
            if nu==0:  
                pass  
            #取消关注  
            map(api.destroy_friendship,on)  
            info="恭喜您已成功取消关注%d位用户....." %nu  
            return render_template('success.html',info=info.decode('utf-8'))  
        except:  
             info="亲,系统繁忙,请稍后再试......,系统在3秒后自动返回..."  
             return render_template('error.html',info=info.decode('utf-8'))  
  
if __name__=='__main__':  
     """ 
     启动app,启动s线程去搜索数据 
     """  
     s=Setag()  
     s.start()  
     app.run()  