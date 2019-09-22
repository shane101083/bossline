# -*- coding: utf-8 -*-
from Linephu.linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,timeit,atexit
from gtts import gTTS
from googletrans import Translator
botStart = time.time()
cl = LINE("yeechen677@gmail.com","yee101083")
kicker01 = LINE("930301line@gmail.com","landy8671")
kicker02 = LINE("9303line@gmail.com","landy8671")
kicker03 = LINE("line930301@gmail.com","landy8671")
kicker04 = LINE("lime9303@gmail.com","landy8671")
kicker05 = LINE("benaon20040301@gmail.com","landy8671")
kicker06 = LINE("ss69696988@gmail.com","aa996988")
kicker07 = LINE("a99632114@gmail.com","landy8671")
kicker08 = LINE("landy950819@gmail.com","landy8671")
kicker09 = LINE("landy50355@gmail.com","landy8671")
kicker10 = LINE("landy94love69@gmail.com","landy8671")
kicker11 = LINE("landy9450355@gmail.com","landy8671")
print ("======登入成功=====")
oepoll = OEPoll(cl)
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
clMID = cl.profile.mid
kicker01MID = kicker01.profile.mid
kicker02MID = kicker02.profile.mid
kicker03MID = kicker03.profile.mid
kicker04MID = kicker04.profile.mid
kicker05MID = kicker05.profile.mid
kicker06MID = kicker06.profile.mid
kicker07MID = kicker07.profile.mid
kicker08MID = kicker08.profile.mid
kicker09MID = kicker09.profile.mid
kicker10MID = kicker10.profile.mid
kicker11MID = kicker11.profile.mid
KAC = [kicker01,kicker02,kicker03,kicker04,kicker05,kicker06,kicker07,kicker08,kicker09,kicker10,kicker11]
admin = ['u79d8b3bd54f20733f9725edfde951305',clMID,kicker01MID,kicker02MID,kicker03MID,kicker04MID,kicker05MID,kicker06MID,kicker07MID,kicker08MID,kicker09MID,kicker10MID,kicker11MID]
gom = ['u79d8b3bd54f20733f9725edfde951305']
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
}
wait = {
      "ban":False,
	  "unban":False,
      "rapidFire":{},	    
      "beunban":False,  	  
      "beban":False,
      "op": False,	  
      "unop": False,	  
      "rapidFire":{}	  
}
setTime = {}
setTime = wait2['setTime']
msg_dict = {}
bl = [""]
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def restartBot():
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invaliod mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
            textx += str(texts[len(mids)])		
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def logError(text):
    cl.log("[ 錯誤 ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def helpmessage():
    helpMessage = """♥ ✿ 指令表 ✿ ♥
查看指令表
╠❂➣【help】指令表
╠❂➣【ag】保護
╠❂➣【gh】狀態
╠❂➣【bh】黑單"""
    return helpMessage
def ahmessage():
    ahMessage ="""╠══✪保護指令✪════
╠❂➣【Leave On/Off】自動離開副本 打開/關閉
╠❂➣【Read On/Off】自動已讀 打開/關閉
╠❂➣【網址 開/關】網址保護 打開/關閉
╠❂➣【踢人 開/關】群組保護 打開/關閉
╠❂➣【保護 開/關】所有保護 打開/關閉
╠❂➣【Reread On/Off】查看收回 打開/關閉"""
    return ahMessage
def ghmessage():
    ghMessage ="""╠══✪狀態指令✪════
╠❂➣【Re】重新啟動機器
╠❂➣【Runtime】查看機器運行時間
╠❂➣【Sp】查看機器速度
╠❂➣【Set】查看設定
╠❂➣【About】查看自己的狀態
╠❂➣【K1-K12 About】查看機器的狀態
╠❂➣【tagall】全標(亂玩永黑處理)
╠❂➣【All join】機器進群(要少空格)
╠❂➣【botbye】機器退群
╠❂➣【設定】設置已讀點
╠❂➣【刪除】刪除讀點
╠❂➣【偵測】偵測已讀"""
    return ghMessage
def bhmessage():
    bhMessage ="""╠══✪黑單指令✪════
╠❂➣【TK @】踢人
╠❂➣【Unban @】標注解除
╠❂➣【Ban @】標註加入黑單
╠❂➣【清空黑單】清除全部黑單
╠❂➣【黑單/永黑】查看黑單
╠❂➣【Kill Ban】踢出黑單"""
    return bhMessage
	
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            contact = cl.getContact(param2)
            print ("[ 5 ] 通知添加好友 名字: " + contact.displayName)
            if settings["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                kicker01.findAndAddContactsByMid(op.param1)
                kicker02.findAndAddContactsByMid(op.param1)
                kicker03.findAndAddContactsByMid(op.param1)
                kicker04.findAndAddContactsByMid(op.param1)
                kicker05.findAndAddContactsByMid(op.param1)
                kicker06.findAndAddContactsByMid(op.param1)
                kicker07.findAndAddContactsByMid(op.param1)
                kicker08.findAndAddContactsByMid(op.param1)
                kicker09.findAndAddContactsByMid(op.param1)
                kicker010.findAndAddContactsByMid(op.param1)
                kicker011.findAndAddContactsByMid(op.param1)
                kicker.findAndAddContactsByMid(op.param1)
                cl.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 ".format(str(cl.getContact(op.param1).displayName)))
                kicker01.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 ".format(str(cl.getContact(op.param1).displayName)))
                kicker02.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 ".format(str(cl.getContact(op.param1).displayName)))
                kicker03.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 ".format(str(cl.getContact(op.param1).displayName)))
                kicker04.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 ".format(str(cl.getContact(op.param1).displayName)))
                kicker05.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 ".format(str(cl.getContact(op.param1).displayName)))
                kicker06.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 ".format(str(cl.getContact(op.param1).displayName)))
                kicker07.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 ".format(str(cl.getContact(op.param1).displayName)))
                kicker08.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 ".format(str(cl.getContact(op.param1).displayName)))
                kicker09.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 ".format(str(cl.getContact(op.param1).displayName)))
                kicker10.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 ".format(str(cl.getContact(op.param1).displayName)))
                kicker11.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 ".format(str(cl.getContact(op.param1).displayName)))
        if op.type == 60:
            if op.param2 in settings['blacklist']:
                cl.sendMessage(op.param1, "[警告]\n此人位於黑名單中! ! !")
                KAC=[kicker01,kicker02,kicker03,kicker04,kicker05,kicker06,kicker07,kicker08,kicker09,kicker10,kicker11]
                kee=random.choice(KAC)				
                kee.acceptGroupInvitationByTicket(op.param1, Ti)
                kee.kickoutFromGroup(op.param1,[op.param2])
            if op.param2 in settings['blacklistbot']:
                cl.sendMessage(op.param1, "[警告]\n此人位於永黑中! ! !")
                KAC=[kicker01,kicker02,kicker03,kicker04,kicker05,kicker06,kicker07,kicker08,kicker09,kicker10,kicker11]
                kee=random.choice(KAC)
                kee.acceptGroupInvitationByTicket(op.param1, Ti)
                kee.kickoutFromGroup(op.param1,[op.param2])				
        if op.type == 11:
            group = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            print ("[11]有人打開群組網址 群組名稱: " + str(group.name) + "\n" + op.param1 + "\n名字: " + contact.displayName)
            if settings["qrprotect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    G = cl.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    cl.updateGroup(G)
                    range.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            if msg.contentType == 7:
               if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    path = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png;compress=true".format(stk_id)
                    ret_ = "[ 貼圖資料 ]"
                    ret_ += "\n貼圖ID : {}".format(stk_id)
                    ret_ += "\n貼圖包ID : {}".format(pkg_id)
                    ret_ += "\n貼圖網址 : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n貼圖圖片網址：https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png;compress=true".format(stk_id)
                    ret_ += "\n[ 完 ]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
        if op.type == 15:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            if settings["seeLeave"] == True:
                try:
                    arrData = ""
                    text = "%s "%('[提示]')
                    arr = []
                    mention = "@x "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + "退出了 {} ！".format(str(group.name))
                    cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)
        if op.type == 25 or op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if wait["ban"] == True:
                    if msg._from in admin:
                        if msg.contentMetadata["mid"] in settings["blacklist"]:
                            cl.sendMessage(msg.to,"已加入黑單")
                            wait["ban"] = False
                        else:
                            settings["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["ban"] = False
                            cl.sendMessage(msg.to,"ok")
                elif wait["unban"] == True:
                    if msg._from in admin:
                        if msg.contentMetadata["mid"] not in settings["blacklist"]:
                            cl.sendMessage(msg.to,"黑單內查無此人")
                            wait["unban"] = False
                        else:
                            del settings["blacklist"][msg.contentMetadata["mid"]]
                            wait["unban"] = False
                            cl.sendMessage(msg.to,"ok")
            if msg.contentType == 13:
                if wait["beban"] == True:
                    if msg._from in admin:
                        if msg.contentMetadata["mid"] in settings["blacklistbot"]:
                            cl.sendMessage(msg.to,"已加入永黑")
                            wait["beban"] = False
                        else:
                            settings["blacklistbot"][msg.contentMetadata["mid"]] = True
                            wait["beban"] = False
                            cl.sendMessage(msg.to,"ok")
                elif wait["beunban"] == True:
                    if msg._from in admin:
                        if msg.contentMetadata["mid"] not in settings["blacklistbot"]:
                            cl.sendMessage(msg.to,"永黑內查無此人")
                            wait["beunban"] = False
                        else:
                            del settings["blacklistbot"][msg.contentMetadata["mid"]]
                            wait["beunban"] = False
                            cl.sendMessage(msg.to,"ok")	
            if msg.contentType == 13:
                if wait["op"] == True:
                    if msg._from in admin:
                        if msg.contentMetadata["mid"] in settings["admin"]:
                            cl.sendMessage(msg.to,"already")
                            wait["op"] = False
                        else:
                            settings["admin"][msg.contentMetadata["mid"]] = True
                            wait["op"] = False
                            cl.sendMessage(msg.to,"ok")
                elif wait["unop"] == True:
                    if msg._from in admin:
                        if msg.contentMetadata["mid"] not in settings["admin"]:
                            cl.sendMessage(msg.to,"already")
                            wait["unop"] = False
                        else:
                            del settings["admin"][msg.contentMetadata["mid"]]
                            wait["unop"] = False
                            cl.sendMessage(msg.to,"ok")				
        if op.type == 13:
            contact1 = cl.getContact(op.param2)
            contact2 = cl.getContact(op.param3)
            group = cl.getGroup(op.param1)
            print ("[ 13 ] 通知邀請群組: " + str(group.name) + "\n邀請者: " + contact1.displayName + "\n被邀請者" + contact2.displayName)
            if settings["inviteprotect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param3)
                    range.choice(KAC).sendMessage(op.param1, "禁止邀請")
                    range.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 13:
            if clMID in op.param3:
                group = cl.getGroup(op.param1)
                if op.param2 in settings["admin"] or op.param2 in gom :
                    cl.acceptGroupInvitation(op.param1)
                    sendMention(op.param1, "權限者 @! 邀請入群",[op.param2])					
                else:
                    cl.acceptGroupInvitation(op.param1)
                    sendMention(op.param1, "@! 你不是權限者",[op.param2])
                    cl.leaveGroup(op.param1)
        if op.type == 25 or op.type == 26:
            msg = op.message
            if  msg.text.lower() == '/ti/g/':
                if settings["autoJoinTicket"] == True:
                    link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = link_re.findall(text)
                    n_links = []
                    for l in links:
                        if l not in n_links:
                            n_links.append(l)
                    for ticket_id in n_links:
                        group = trev.findGroupByTicket(ticket_id)
                        cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                        kicker01.acceptGroupInvitationByTicket(group.id, ticket_id)
                        kicker02.acceptGroupInvitationByTicket(group.id, ticket_id)
                        kicker03.acceptGroupInvitationByTicket(group.id, ticket_id)
                        kicker04.acceptGroupInvitationByTicket(group.id, ticket_id)
                        kicker05.acceptGroupInvitationByTicket(group.id, ticket_id)
                        kicker06.acceptGroupInvitationByTicket(group.id, ticket_id)
                        kicker07.acceptGroupInvitationByTicket(group.id, ticket_id)
                        kicker08.acceptGroupInvitationByTicket(group.id, ticket_id)
                        kicker09.acceptGroupInvitationByTicket(group.id, ticket_id)
                        kicker10.acceptGroupInvitationByTicket(group.id, ticket_id)
                        kicker11.acceptGroupInvitationByTicket(group.id, ticket_id)
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
				
        if op.type == 19:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            contact2 = cl.getContact(op.param3)
            print ("[19]有人把人踢出群組 群組名稱: " + str(group.name) + "\n" + op.param1 +"\n踢人者: " + contact1.displayName + "\nMid: " + contact1.mid + "\n被踢者" + contact2.displayName + "\nMid:" + contact2.mid )
            if op.param1 in settings["protect"]:
                if op.param2 in admin or op.param2 in settings["admin"] or op.param2 in group.creator:
                    pass
                else:
                    WWWW=[cl,kicker01,kicker02,kicker03,kicker04,kicker05,kicker06,kicker07,kicker08,kicker09,kicker10,kicker11]
                    k1235=random.choice(WWWW)
                    k1235.kickoutFromGroup(op.param1,[op.param2])
                    k1235.inviteIntoGroup(op.param1,["u4adfe266bf25f55cb801a2505dbbfd8c"])
                    settings["blacklist"][op.param2] = True
            else:
                pass
            if clMID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker01.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進永久黑名單。")
                        if op.param2 in settings["blacklistbot"]:
                            pass
                        else:
                            settings["blacklistbot"][op.param2] = True
                    G = kicker01.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker01.updateGroup(G)
                    invsend = 0
                    Ti = kicker01.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker11.acceptGroupInvitationByTicket(op.param1, Ti)     
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
            if kicker01MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker01.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進永久黑名單。")
                        if op.param2 in settings["blacklistbot"]:
                            pass
                        else:
                            settings["blacklistbot"][op.param2] = True
                    G = kicker01.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker01.updateGroup(G)
                    invsend = 0
                    Ti = kicker01.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker11.acceptGroupInvitationByTicket(op.param1, Ti)     
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
            if kicker02MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker01.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進永久黑名單。")
                        if op.param2 in settings["blacklistbot"]:
                            pass
                        else:
                            settings["blacklistbot"][op.param2] = True
                    G = kicker01.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker01.updateGroup(G)
                    invsend = 0
                    Ti = kicker01.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker11.acceptGroupInvitationByTicket(op.param1, Ti)     
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
            if kicker03MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker01.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進永久黑名單。")
                        if op.param2 in settings["blacklistbot"]:
                            pass
                        else:
                            settings["blacklistbot"][op.param2] = True
                    G = kicker01.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker01.updateGroup(G)
                    invsend = 0
                    Ti = kicker01.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker11.acceptGroupInvitationByTicket(op.param1, Ti)     
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
            if kicker04MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker01.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進永久黑名單。")
                        if op.param2 in settings["blacklistbot"]:
                            pass
                        else:
                            settings["blacklistbot"][op.param2] = True
                    G = kicker01.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker01.updateGroup(G)
                    invsend = 0
                    Ti = kicker01.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker11.acceptGroupInvitationByTicket(op.param1, Ti)     
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
            if kicker05MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker01.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進永久黑名單。")
                        if op.param2 in settings["blacklistbot"]:
                            pass
                        else:
                            settings["blacklistbot"][op.param2] = True
                    G = kicker01.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker01.updateGroup(G)
                    invsend = 0
                    Ti = kicker01.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker11.acceptGroupInvitationByTicket(op.param1, Ti)     
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
            if kicker06MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker01.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進永久黑名單。")
                        if op.param2 in settings["blacklistbot"]:
                            pass
                        else:
                            settings["blacklistbot"][op.param2] = True
                    G = kicker01.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker01.updateGroup(G)
                    invsend = 0
                    Ti = kicker01.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker11.acceptGroupInvitationByTicket(op.param1, Ti)     
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)				
            if kicker07MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker01.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進永久黑名單。")
                        if op.param2 in settings["blacklistbot"]:
                            pass
                        else:
                            settings["blacklistbot"][op.param2] = True
                    G = kicker01.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker01.updateGroup(G)
                    invsend = 0
                    Ti = kicker01.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker11.acceptGroupInvitationByTicket(op.param1, Ti)     
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
            if kicker08MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker01.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進永久黑名單。")
                        if op.param2 in settings["blacklistbot"]:
                            pass
                        else:
                            settings["blacklistbot"][op.param2] = True
                    G = kicker01.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker01.updateGroup(G)
                    invsend = 0
                    Ti = kicker01.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker11.acceptGroupInvitationByTicket(op.param1, Ti)     
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
            if kicker09MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker01.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進永久黑名單。")
                        if op.param2 in settings["blacklistbot"]:
                            pass
                        else:
                            settings["blacklistbot"][op.param2] = True
                    G = kicker01.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker01.updateGroup(G)
                    invsend = 0
                    Ti = kicker01.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker11.acceptGroupInvitationByTicket(op.param1, Ti)     
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
#===========================================================================================================================================================================#
            if kicker10MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker01.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進永久黑名單。")
                        if op.param2 in settings["blacklistbot"]:
                            pass
                        else:
                            settings["blacklistbot"][op.param2] = True
                    G = kicker01.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker01.updateGroup(G)
                    invsend = 0
                    Ti = kicker01.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker11.acceptGroupInvitationByTicket(op.param1, Ti)     
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
            if kicker11MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker01.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進永久黑名單。")
                        if op.param2 in settings["blacklistbot"]:
                            pass
                        else:
                            settings["blacklistbot"][op.param2] = True
                    G = kicker01.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker01.updateGroup(G)
                    invsend = 0
                    Ti = kicker01.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)     
                    kicker11.acceptGroupInvitationByTicket(op.param1, Ti)     
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
        if op.type == 24:
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1)
                kicker01.leaveRoom(op.param1)
                kicker02.leaveRoom(op.param1)
                kicker03.leaveRoom(op.param1)
                kicker04.leaveRoom(op.param1)
                kicker05.leaveRoom(op.param1)
                kicker06.leaveRoom(op.param1)
                kicker07.leaveRoom(op.param1)
                kicker08.leaveRoom(op.param1)
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 13:
                if settings["contact"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                            cl.sendMessage(msg.to,"[顯示名稱]:\n" + msg.contentMetadata["顯示名稱"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[狀態消息]:\n" + contact.statusMessage + "\n[圖片網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendMessage(msg.to,"[顯示名稱]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[狀態消息]:\n" + contact.statusMessage + "\n[圖片網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu))
            elif msg.contentType == 16:
                if settings["timeline"] == True:
                    try:
                        msg.contentType = 0
                        f_mid = msg.contentMetadata["postEndUrl"].split("userMid=")
                        s_mid = f_mid[1].split("&")
                        mid = s_mid[0]
                        try:
                            arrData = ""
                            text = "%s\n%s\n"%("---[分享文章預覽]---","[文章作成者]:")
                            arr = []
                            mention = "@x "
                            slen = str(len(text))
                            elen = str(len(text) + len(mention) - 1)
                            arrData = {'S':slen, 'E':elen, 'M':mid}
                            arr.append(arrData)
                            text += mention + "\n[文字預覽]:\n" + msg.contentMetadata["text"] + "\n(僅顯示100字)" + "\n[文章網址]:\n" + msg.contentMetadata["postEndUrl"]
                            cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        except Exception as error:
                            print(error)
                    except:
                        ret_ = "---[群組文章預覽]---\n[文字預覽]:\n" + msg.contentMetadata["text"] + "\n(僅顯示100字)"
                        ret_ += "\n[文章網址]:\n" + msg.contentMetadata["postEndUrl"]
                        cl.sendMessage(msg.to, str(ret_))
            if msg.contentType == 0:
                if text is None:
                    return
                elif "Kickall" in msg.text:
                    if settings["kickmeber"] == True:
                        if msg.toType == 2:
                            _name = msg.text.replace("Kickall","")
                            gs = cl.getGroup(to)
                            cl.sendMessage(to, "老爺愛愛降臨")
                            targets = []
                            for g in gs.members:
                                if _name in g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                pass
                            else:
                                for target in targets:
                                    if target in admin:
                                        pass
                                    else:
                                        try:
                                            klist=[kicker01,kicker02,kicker03,kicker04,kicker05,kicker06,kicker07,kicker08,kicker09,kicker10,kicker11]
                                            kicker=random.choice(klist)
                                            kicker.kickoutFromGroup(to, [target])
                                        except:
                                            pass
                elif text.startswith('自動清空'):				
                    cl.sendMessage(to, "Automatic emptying!!!!!")					
                    cl.removeAllMessages(op.param2)
                    kicker01.removeAllMessages(op.param2)
                    kicker02.removeAllMessages(op.param2)
                    kicker03.removeAllMessages(op.param2)
                    kicker04.removeAllMessages(op.param2)
                    kicker05.removeAllMessages(op.param2)
                    kicker06.removeAllMessages(op.param2)
                    kicker07.removeAllMessages(op.param2)
                    kicker08.removeAllMessages(op.param2)
                    kicker09.removeAllMessages(op.param2)
                    kicker10.removeAllMessages(op.param2)
                    kicker11.removeAllMessages(op.param2)
                    cl.sendMessage(to, "Success deleted allMessage for this room")					
                elif text.lower() == '創群':
                    group = cl.getGroup(to)
                    GS = group.creator.mid
                    cl.sendContact(to, GS)
                elif msg.text.lower().startswith("友資 "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            mi_d = contact.mid
                            cl.sendContact(msg.to, mi_d)
                elif text.lower() == 'bot/bye':
                    if msg.toType == 2:
                        ginfo = cl.getGroup(to)
                        try:
                            cl.leaveGroup(to)							
                        except:
                            pass	
                elif text.lower().startswith('add '):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["admin"][target] = True
                            cl.sendMessage(msg.to,"已加入權限!")
                            break
                        except:
                            cl.sendMessage(msg.to,"添加失敗 !")
                            break
                elif text.lower().startswith('del '):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["admin"][target]
                            cl.sendMessage(msg.to,"刪除權限成功 !")
                            break
                        except:
                            cl.sendMessage(msg.to,"刪除失敗 !")
                            break
                elif text.lower() == 'op':
                    cl.sendMessage(to, "請傳送友資加入權限")
                    wait["op"] = True
                elif text.lower() == 'unop':
                    cl.sendMessage(to, "請傳送友資移除權限")
                    wait["unop"] = True
                elif text.lower().startswith('add:'):
                        midd = msg.text.replace("add:","")
                        admin.append(str(midd))
                        cl.sendMessage(to, "已加入權限！") 
                        backupData()
                elif text.lower().startswith('del:'):
                        midd = msg.text.replace("del:","")
                        admin.remove(str(midd))
                        cl.sendMessage(to, "已刪除權限！") 
                        backupData()					
            if sender in admin or sender in settings["admin"] or sender in gom :
                if text.lower() == 'help':
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage))
                elif text.lower() == 'ah':
                    ahMessage = ahmessage()
                    cl.sendMessage(to, str(ahMessage))
                elif text.lower() == 'gh':
                    ghMessage = ghmessage()
                    cl.sendMessage(to, str(ghMessage))
                elif text.lower() == 'bh':
                    bhMessage = bhmessage()
                    cl.sendMessage(to, str(bhMessage))
                elif text.lower() == 'adminlist':
                    if admin == []:
                        cl.sendMessage(to, "沒有權限者")
                    else:
                        mc = "權限者清單："
                        for mi_d in settings["admin"]:
                            mc += "\n-> " +cl.getContact(mi_d).displayName
                        cl.sendMessage(to, mc)	
                elif text.lower() == '運行':
                    cl.sendMessage(to,'1')
                    kicker01.sendMessage(to, '2')
                    kicker02.sendMessage(to, '3')
                    kicker03.sendMessage(to, '4')
                    kicker04.sendMessage(to, '5')	
                    kicker05.sendMessage(to, '6')
                    kicker06.sendMessage(to, '7')					
                    kicker07.sendMessage(to, '8')
                    kicker08.sendMessage(to, '9')
                    kicker09.sendMessage(to, '10')
                    kicker10.sendMessage(to, '11')
                    kicker11.sendMessage(to, '12')						
                elif 'alljoin' in text.lower():
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            cl.updateGroup(G)
                            invsend = 0
                            Ti = cl.reissueGroupTicket(to)
                            kicker01.acceptGroupInvitationByTicket(to, Ti)
                            kicker02.acceptGroupInvitationByTicket(to, Ti)
                            kicker03.acceptGroupInvitationByTicket(to, Ti)
                            kicker04.acceptGroupInvitationByTicket(to, Ti)
                            kicker05.acceptGroupInvitationByTicket(to, Ti)
                            kicker06.acceptGroupInvitationByTicket(to, Ti)
                            kicker07.acceptGroupInvitationByTicket(to, Ti)
                            kicker08.acceptGroupInvitationByTicket(to, Ti)
                            kicker09.acceptGroupInvitationByTicket(to, Ti)
                            kicker10.acceptGroupInvitationByTicket(to, Ti)
                            kicker11.acceptGroupInvitationByTicket(to, Ti)
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                        else:
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                            invsend = 0
                            Ti = cl.reissueGroupTicket(to)
                            kicker01.acceptGroupInvitationByTicket(to, Ti)
                            kicker02.acceptGroupInvitationByTicket(to, Ti)
                            kicker03.acceptGroupInvitationByTicket(to, Ti)
                            kicker04.acceptGroupInvitationByTicket(to, Ti)	
                            kicker05.acceptGroupInvitationByTicket(to, Ti)
                            kicker06.acceptGroupInvitationByTicket(to, Ti)
                            kicker07.acceptGroupInvitationByTicket(to, Ti)							
                            kicker08.acceptGroupInvitationByTicket(to, Ti)							
                            kicker09.acceptGroupInvitationByTicket(to, Ti)
                            kicker10.acceptGroupInvitationByTicket(to, Ti)							
                            kicker11.acceptGroupInvitationByTicket(to, Ti)							
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                elif text.lower() == 'botbye':
                    if msg.toType == 2:
                        ginfo = cl.getGroup(to)
                        try:
                            kicker01.leaveGroup(to)
                            kicker02.leaveGroup(to)
                            kicker03.leaveGroup(to)
                            kicker04.leaveGroup(to)
                            kicker05.leaveGroup(to)
                            kicker06.leaveGroup(to)
                            kicker07.leaveGroup(to)							
                            kicker08.leaveGroup(to)							
                            kicker09.leaveGroup(to)
                            kicker10.leaveGroup(to)							
                            kicker11.leaveGroup(to)														
                        except:
                            pass

                elif text.lower() == 'beban':
                    cl.sendMessage(to, "請傳送友資加入永黑")
                    wait["beban"] = True
                elif text.lower() == 'beunban':
                    cl.sendMessage(to, "請傳送友資移除永黑")
                    wait["beunban"] = True	
                elif text.lower() == 'ban':
                    cl.sendMessage(to, "請傳送友資加入黑名單")
                    wait["ban"] = True
                elif text.lower() == 'unban':
                    cl.sendMessage(to, "請傳送友資移除黑名單")
                    wait["unban"] = True
                elif "Mb:" in msg.text:
                    midd = msg.text.replace("ban:","")
                    try:
                        settings["blacklist"][midd] = True
                        backupData()
                        cl.sendMessage(to, "已加入黑名單")
                    except:
                        pass
                elif "Mub:" in msg.text:
                    midd = msg.text.replace("unban:","")
                    try:
                        del settings["blacklist"][midd]
                        backupData()
                        cl.sendMessage(to, "已解除黑名單")
                    except:
                        pass					
                elif text.lower() == '永黑':
                    if settings["blacklistbot"] == {}:
                        cl.sendMessage(msg.to,"無永黑單成員!")
                    else:
                        mc = "╔══[ 永黑 ]"
                        no = 0						
                        for mi_d in settings["blacklistbot"]:
                            no += 1						
                            mc += "\n╠{}.".format(str(no))+cl.getContact(mi_d).displayName
                        cl.sendMessage(msg.to,mc +"\n╚══[總共"+str(len(settings["blacklistbot"]))+ "個人被黑單]")
                elif text.lower() == '永黑mid':
                    if settings["blacklistbot"] == {}:
                        cl.sendMessage(msg.to,"無永黑單成員!")
                    else:
                        mc = "╔══[ 永黑mid ]"
                        no = 0						
                        for mi_d in settings["blacklistbot"]:
                            no += 1						
                            mc += "\n╠{}.".format(str(no))+(mi_d)
                        cl.sendMessage(msg.to,mc +"\n╚══[總共"+str(len(settings["blacklistbot"]))+ "個人被黑單]")						
                elif msg.text in ["c","C","cancel","Cancel"]:
                  if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = (contact.mid for contact in X.invitee)
                        ginfo = cl.getGroup(msg.to)
                        sinvitee = str(len(ginfo.invitee))
                        start = time.time()
                        for cancelmod in gInviMids:
                            cl.cancelGroupInvitation(msg.to, [cancelmod])
                        elapsed_time = time.time() - start
                        cl.sendMessage(to, "已取消完成\n取消時間: %s秒" % (elapsed_time))
                        cl.sendMessage(to, "取消人數:" + sinvitee)
                    else:
                        cl.sendMessage(to, "沒有任何人在邀請中！！")
                elif "Ban" in msg.text:
                    if msg.toType == 2:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    settings["blacklist"][target] = True
                                    cl.sendMessage(to, "已加入黑名單")
                                except:
                                    pass
                elif "Unban" in msg.text:
                    if msg.toType == 2:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    del settings["blacklist"][target]
                                    cl.sendMessage(to, "已解除黑名單")
                                except:
                                    pass
                elif text.lower() == '清空黑單':
                    for mi_d in settings["blacklist"]:
                        settings["blacklist"] = {}
                    cl.sendMessage(to, "已清空黑名單")
                if text.lower() in ['黑單','黑']:
                    if settings["blacklist"] == {}:
                        cl.sendMessage(msg.to,"無黑單成員!")
                    else:
                        mc = "╔══[ 黑名單 ]"
                        for mi_d in settings["blacklist"]:
                            mc += "\n╠ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(msg.to,mc +"\n╚══[總共"+str(len(settings["blacklist"]))+ "個人被黑單]")
                if text.lower() == '黑單mid':
                    if settings["blacklist"] == {}:
                        cl.sendMessage(msg.to,"無黑單成員!")
                    else:
                        mc = "╔══[ 黑名單 ]"
                        for mi_d in settings["blacklist"]:
                            mc += "\n╠ "+(mi_d)
                        cl.sendMessage(msg.to,mc +"\n╚══[總共"+str(len(settings["blacklist"]))+ "個人被黑單]")						
                elif text.lower() == 'kill beban':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in settings["blacklistbot"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            cl.sendMessage(to, "沒有永單")
                        klist = [kicker01,kicker02,kicker03,kicker04,kicker05,kicker06,kicker07,kicker08,kicker09,kicker10,kicker11]
                        kickers = random.choice(klist)
                        for jj in matched_list:
                            kickers.kickoutFromGroup(to, [jj])
                        cl.sendMessage(to, "永單以踢除")
                elif text.lower() == 'kill ban':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in settings["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            cl.sendMessage(to, "沒有黑名單")
                        klist = [kicker01,kicker02,kicker03,kicker04,kicker05,kicker06,kicker07,kicker08]
                        kickers = random.choice(klist)
                        for jj in matched_list:
                            kickers.kickoutFromGroup(to, [jj])
                        cl.sendMessage(to, "黑名單以踢除")
                elif msg.text in ["全群掃黑"]:
                    gid = cl.getGroupIdsJoined()
                    ban_list = []
                    for tag in settings["blacklist"]:
                        ban_list += filter(lambda str: str == tag, gMembMids)
                    if ban_list == []:
                        cl.sendMessage(to, "沒有黑名單")
                    else:
                        for i in gid:
                            for jj in ban_list:
                                cl.kickoutFromGroup(i, [jj])
                            cl.sendMessage(i, "掃黑結束")
                elif text.lower() == '報數':
                    cl.sendMessage(to,'幹')
                    kicker01.sendMessage(to, '你')
                    kicker02.sendMessage(to, '娘')
                    kicker03.sendMessage(to, '擊')
                    kicker04.sendMessage(to, '掰')	
                    kicker05.sendMessage(to, '操')
                    kicker06.sendMessage(to, '愛')					
                    kicker07.sendMessage(to, '情')
                    kicker08.sendMessage(to, '都')
                    kicker09.sendMessage(to, '是')
                    kicker10.sendMessage(to, '假')
                    kicker11.sendMessage(to, '的')
                elif "Mc " in msg.text:
                    mmid = msg.text.replace("Mc ","")
                    cl.sendContact(to, mmid)
                elif msg.text.lower().startswith("頭貼"):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + cl.getContact(ls).pictureStatus
                            cl.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("封面"):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = cl.getProfileCoverURL(ls)
                                cl.sendImageWithURL(msg.to, str(path))
                elif text.lower() == '日期':
                    tz = pytz.timezone("Asia/Makassar")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["星期天", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = timeNow.strftime('%Y') + "/" + bln + "/" + timeNow.strftime('%d') + (" 【") + hasil + ("】 ") + "\n時間 : " + timeNow.strftime('%H:%M:%S')
                    cl.sendMessage(msg.to, readTime)
                elif "踢 " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        if target in admin:
                            pass
                        else:
                            try:
                                 klist=[kicker01,kicker02,kicker03,kicker04,kicker05,kicker06,kicker07,kicker08,kicker09,kicker10,kicker11]
                                 kicker=random.choice(klist)
                                 kicker.kickoutFromGroup(to, [target])							
                            except:
                                pass
                elif text.lower() == 'me':
                    if msg.toType == 2 or msg.toType == 1:
                        sendMessageWithMention(to, sender)
                        cl.sendContact(to, sender)
                    else:
                        cl.sendContact(to,sender)
                elif text.lower() == 'mymid':
                    cl.sendMessage(msg.to,"[MID]\n" +  sender)
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = ""
                        for ls in lists:
                            ret_ += ls
                        cl.sendMessage(msg.to, str(ret_))										
                elif text.lower() == 'botkgban':
                    gid = cl.getGroupIdsJoined() 
                    for i in gid:
                        group=cl.getGroup(i)
                        gMembMids = [contact.mid for contact in group.members] 
                        ban_list = [] 
                        for tag in settings["blacklistbot"]: 
                            ban_list += filter(lambda str: str == tag, gMembMids) 
                        if ban_list == []: 
                            cl.sendMessage(i, "沒有黑名單") 
                        else: 
                            for jj in ban_list: 
                                cl.kickoutFromGroup(i, [jj]) 
                            cl.sendMessage(i, "掃黑結束") 								
                elif text.lower() == 'kgban':
                    gid = cl.getGroupIdsJoined() 
                    for i in gid:
                        group=cl.getGroup(i)
                        gMembMids = [contact.mid for contact in group.members] 
                        ban_list = [] 
                        for tag in settings["blacklist"]: 
                            ban_list += filter(lambda str: str == tag, gMembMids) 
                        if ban_list == []: 
                            cl.sendMessage(i, "沒有黑名單") 
                        else: 
                            for jj in ban_list: 
                                cl.kickoutFromGroup(i, [jj]) 
                            cl.sendMessage(i, "掃黑結束")
                elif text.lower() == 'tagall':
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                elif text.lower() == '設定':
                    cl.sendMessage(msg.to, "已讀點設置成功")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                elif text.lower() == "刪除":
                    cl.sendMessage(to, "已讀點已刪除")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                        del wait2['setTime'][msg.to]
                    except:
                        pass
                elif msg.text in ["偵測","偵測已讀"]:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"
                        cl.sendMessage(msg.to, "[已讀順序]%s\n\n[已讀的人]:\n%s\n查詢時間:[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendMessage(msg.to, "請輸入setread")
                elif "Fbc:" in msg.text:
                    bctxt = text.replace("Fbc:","")
                    t = cl.getAllContactIds()
                    for manusia in t:
                        cl.sendMessage(manusia,(bctxt))
                elif "Gbc:" in msg.text:
                    bctxt = text.replace("Gbc:","")
                    n = cl.getGroupIdsJoined()
                    for manusia in n:
                        cl.sendMessage(manusia,(bctxt))
                elif text.lower() == 'sp':
                    start = time.time()
                    cl.sendMessage(to, "檢查中...")
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,format(str(elapsed_time)) + "秒")		
                elif text.lower() == 'save':
                    backupData()
                    cl.sendMessage(to,"儲存設定成功!")

                elif text.lower() == 're':
                    cl.sendMessage(to, "重新啟動")
                    restartBot()
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    cl.sendMessage(to, "機器運行時間 {}".format(str(runtime)))
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "u28d781fa3ba9783fd5144390352b0c24"
                        creator = cl.getContact(owner)
                        contact = cl.getContact(clMID)
                        grouplist = cl.getGroupIdsJoined()
                        contactlist = cl.getAllContactIds()
                        blockedlist = cl.getBlockedContactIds()
                        ret_ = "╔══[ 關於自己 ]"
                        ret_ += "\n╠ 名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 黑單 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於機器 ]"
                        ret_ += "\n╠ 版本 : 主機"
                        ret_ += "\n╚══[ 未經許可禁止重製 ]"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'k1 about':
                    try:
                        arr = []
                        owner = "u28d781fa3ba9783fd5144390352b0c24"
                        creator = kicker01.getContact(owner)
                        contact = kicker01.getContact(clMID)
                        grouplist = kicker01.getGroupIdsJoined()
                        contactlist = kicker01.getAllContactIds()
                        blockedlist = kicker01.getBlockedContactIds()
                        ret_ = "╔══[ 關於自己 ]"
                        ret_ += "\n╠ 名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 黑單 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於機器 ]"
                        ret_ += "\n╠ 版本 : K1"
                        ret_ += "\n╚══[ 未經許可禁止重製 ]"
                        kicker01.sendMessage(to, str(ret_))
                    except Exception as e:
                        kicker01.sendMessage(msg.to, str(e))
                elif text.lower() == 'k2 about':
                    try:
                        arr = []
                        owner = "u28d781fa3ba9783fd5144390352b0c24"
                        creator = kicker02.getContact(owner)
                        contact = kicker02.getContact(clMID)
                        grouplist = kicker02.getGroupIdsJoined()
                        contactlist = kicker02.getAllContactIds()
                        blockedlist = kicker02.getBlockedContactIds()
                        ret_ = "╔══[ 關於自己 ]"
                        ret_ += "\n╠ 名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 黑單 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於機器 ]"
                        ret_ += "\n╠ 版本 : K2"
                        ret_ += "\n╚══[ 未經許可禁止重製 ]"
                        kicker02.sendMessage(to, str(ret_))
                    except Exception as e:
                        kicker02.sendMessage(msg.to, str(e))
                elif text.lower() == 'k3 about':
                    try:
                        arr = []
                        owner = "u28d781fa3ba9783fd5144390352b0c24"
                        creator = kicker03.getContact(owner)
                        contact = kicker03.getContact(clMID)
                        grouplist = kicker03.getGroupIdsJoined()
                        contactlist = kicker03.getAllContactIds()
                        blockedlist = kicker03.getBlockedContactIds()
                        ret_ = "╔══[ 關於自己 ]"
                        ret_ += "\n╠ 名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 黑單 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於機器 ]"
                        ret_ += "\n╠ 版本 : K3"
                        ret_ += "\n╚══[ 未經許可禁止重製 ]"
                        kicker03.sendMessage(to, str(ret_))
                    except Exception as e:
                        kicker03.sendMessage(msg.to, str(e))
                elif text.lower() == 'k4 about':
                    try:
                        arr = []
                        owner = "u28d781fa3ba9783fd5144390352b0c24"
                        creator =kicker04 .getContact(owner)
                        contact = kicker04.getContact(clMID)
                        grouplist = kicker04.getGroupIdsJoined()
                        contactlist = kicker04.getAllContactIds()
                        blockedlist = kicker04.getBlockedContactIds()
                        ret_ = "╔══[ 關於自己 ]"
                        ret_ += "\n╠ 名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 黑單 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於機器 ]"
                        ret_ += "\n╠ 版本 : K4"
                        ret_ += "\n╚══[ 未經許可禁止重製 ]"
                        kicker04.sendMessage(to, str(ret_))
                    except Exception as e:
                        kicker04.sendMessage(msg.to, str(e))
                elif text.lower() == 'k5 about':
                    try:
                        arr = []
                        owner = "u28d781fa3ba9783fd5144390352b0c24"
                        creator =kicker05 .getContact(owner)
                        contact = kicker05.getContact(clMID)
                        grouplist = kicker05.getGroupIdsJoined()
                        contactlist = kicker05.getAllContactIds()
                        blockedlist = kicker05.getBlockedContactIds()
                        ret_ = "╔══[ 關於自己 ]"
                        ret_ += "\n╠ 名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 黑單 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於機器 ]"
                        ret_ += "\n╠ 版本 : K5"
                        ret_ += "\n╚══[ 未經許可禁止重製 ]"
                        kicker05.sendMessage(to, str(ret_))
                    except Exception as e:
                        kicker05.sendMessage(msg.to, str(e))
                elif text.lower() == 'k6 about':
                    try:
                        arr = []
                        owner = "u28d781fa3ba9783fd5144390352b0c24"
                        creator = kicker06.getContact(owner)
                        contact = kicker06.getContact(clMID)
                        grouplist = kicker06.getGroupIdsJoined()
                        contactlist = kicker06.getAllContactIds()
                        blockedlist = kicker06.getBlockedContactIds()
                        ret_ = "╔══[ 關於自己 ]"
                        ret_ += "\n╠ 名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 黑單 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於機器 ]"
                        ret_ += "\n╠ 版本 : K6"
                        ret_ += "\n╚══[ 未經許可禁止重製 ]"
                        kicker06.sendMessage(to, str(ret_))
                    except Exception as e:
                        kicker06.sendMessage(msg.to, str(e))
                elif text.lower() == 'k7 about':
                    try:
                        arr = []
                        owner = "u28d781fa3ba9783fd5144390352b0c24"
                        creator =kicker07 .getContact(owner)
                        contact = kicker07.getContact(clMID)
                        grouplist = kicker07.getGroupIdsJoined()
                        contactlist = kicker07.getAllContactIds()
                        blockedlist = kicker07.getBlockedContactIds()
                        ret_ = "╔══[ 關於自己 ]"
                        ret_ += "\n╠ 名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 黑單 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於機器 ]"
                        ret_ += "\n╠ 版本 : K7"
                        ret_ += "\n╚══[ 未經許可禁止重製 ]"
                        kicker07.sendMessage(to, str(ret_))
                    except Exception as e:
                        kicker07.sendMessage(msg.to, str(e))
                elif text.lower() == 'k8 about':
                    try:
                        arr = []
                        owner = "u28d781fa3ba9783fd5144390352b0c24"
                        creator = kicker08 .getContact(owner)
                        contact = kicker08.getContact(clMID)
                        grouplist = kicker08.getGroupIdsJoined()
                        contactlist = kicker08.getAllContactIds()
                        blockedlist = kicker08.getBlockedContactIds()
                        ret_ = "╔══[ 關於自己 ]"
                        ret_ += "\n╠ 名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 黑單 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於機器 ]"
                        ret_ += "\n╠ 版本 : K8"
                        ret_ += "\n╚══[ 未經許可禁止重製 ]"
                        kicker08.sendMessage(to, str(ret_))
                    except Exception as e:
                        kicker08.sendMessage(msg.to, str(e))
                elif text.lower() == 'k9 about':
                    try:
                        arr = []
                        owner = "u28d781fa3ba9783fd5144390352b0c24"
                        creator = kicker09 .getContact(owner)
                        contact = kicker09.getContact(clMID)
                        grouplist = kicker09.getGroupIdsJoined()
                        contactlist = kicker09.getAllContactIds()
                        blockedlist = kicker09.getBlockedContactIds()
                        ret_ = "╔══[ 關於自己 ]"
                        ret_ += "\n╠ 名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 黑單 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於機器 ]"
                        ret_ += "\n╠ 版本 : K9"
                        ret_ += "\n╚══[ 未經許可禁止重製 ]"
                        kicker09.sendMessage(to, str(ret_))
                    except Exception as e:
                        kicker09.sendMessage(msg.to, str(e))
                elif text.lower() == 'k10 about':
                    try:
                        arr = []
                        owner = "u28d781fa3ba9783fd5144390352b0c24"
                        creator = kicker10 .getContact(owner)
                        contact = kicker10.getContact(clMID)
                        grouplist = kicker10.getGroupIdsJoined()
                        contactlist = kicker10.getAllContactIds()
                        blockedlist = kicker10.getBlockedContactIds()
                        ret_ = "╔══[ 關於自己 ]"
                        ret_ += "\n╠ 名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 黑單 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於機器 ]"
                        ret_ += "\n╠ 版本 : K10"
                        ret_ += "\n╚══[ 未經許可禁止重製 ]"
                        kicker10.sendMessage(to, str(ret_))
                    except Exception as e:
                        kicker10.sendMessage(msg.to, str(e))
                elif text.lower() == 'k11 about':
                    try:
                        arr = []
                        owner = "u28d781fa3ba9783fd5144390352b0c24"
                        creator = kicker11 .getContact(owner)
                        contact = kicker11.getContact(clMID)
                        grouplist = kicker11.getGroupIdsJoined()
                        contactlist = kicker11.getAllContactIds()
                        blockedlist = kicker11.getBlockedContactIds()
                        ret_ = "╔══[ 關於自己 ]"
                        ret_ += "\n╠ 名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 黑單 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於機器 ]"
                        ret_ += "\n╠ 版本 : K11"
                        ret_ += "\n╚══[ 未經許可禁止重製 ]"
                        kicker11.sendMessage(to, str(ret_))
                    except Exception as e:
                        kicker11.sendMessage(msg.to, str(e))																			
                elif text.lower() == 'set':
                    try:
                        ret_ = "╔══[ 設定 ]"
                        if settings["autoLeave"] == True: ret_ += "\n╠ 自動離開副本 ✅"
                        else: ret_ += "\n╠ 自動離開副本 ❌"
                        if settings["autoRead"] == True: ret_ += "\n╠ 自動已讀 ✅"
                        else: ret_ += "\n╠ 自動已讀 ❌"
                        if msg.toType==2:
                            G = cl.getGroup(msg.to)
                            if G.id in settings["protect"] : ret_+="\n╠ 踢人保護 ✅"
                            else: ret_ += "\n╠ 踢人保護 ❌"
                            if G.id in settings["qrprotect"] : ret_+="\n╠ 網址保護 ✅"
                            else: ret_ += "\n╠ 網址保護 ❌"
                        if settings["detectMention"] == True: ret_ += "\n╠ 標記回復 ✅"
                        else: ret_ += "\n╠ 標記回復 ❌"							
                        if settings["contact"] == True: ret_ += "\n╠ 詳細資料 ✅"
                        else: ret_ += "\n╠ 詳細資料 ❌"
                        if settings["reread"] == True: ret_ += "\n╠ 查詢收回開啟 ✅"
                        else: ret_ += "\n╠ 查詢收回關閉 ❌"
                        ret_ += "\n╚══[ 設定 ]"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'leave on':
                    settings["autoLeave"] = True
                    cl.sendMessage(to, "自動離開副本已開啟")
                elif text.lower() == 'leave off':
                    settings["autoLeave"] = False
                    cl.sendMessage(to, "自動離開副本已關閉")
                elif text.lower() == 'read on':
                    settings["autoRead"] = True
                    cl.sendMessage(to, "自動已讀已開啟")
                elif text.lower() == 'read off':
                    settings["autoRead"] = False
                    cl.sendMessage(to, "自動已讀已關閉")
                elif text.lower() == '文章開':
                    settings["timeline"] = True
                    cl.sendMessage(to, "文章已開啟")
                elif text.lower() == '文章關':
                    settings["timeline"] = False
                    cl.sendMessage(to, "文章已關閉")
                elif text.lower() == '標註回復開':
                    settings["detectMention"] = True
                    cl.sendMessage(to, "已開啟標註偵測")
                elif text.lower() == '標註回復關':
                    settings["detectMention"] = False
                    cl.sendMessage(to, "已關閉標註偵測")

                elif text.lower() == '網址開':
                    if msg.toType ==2:
                        G = cl.getGroup(msg.to)
                        settings["qrprotect"][G.id] = True
                        cl.sendMessage(to, "網址保護開啟")
                elif text.lower() == '網址關':
                    if msg.toType ==2 :
                        G = cl.getGroup(msg.to)
                        try:
                            del settings["qrprotect"][G.id]
                        except:
                            pass
                        cl.sendMessage(to, "網址保護關閉")
                elif text.lower() == '踢人開':
                    if msg.toType ==2:
                        G = cl.getGroup(msg.to)
                        settings["protect"][G.id] = True
                        cl.sendMessage(to, "踢人保護開啟")
                elif text.lower() == '踢人關':
                    if msg.toType ==2 :
                        G = cl.getGroup(msg.to)
                        try:
                            del settings["protect"][G.id]
                        except:
                            pass
                        cl.sendMessage(to, "踢人保護關閉")
                elif text.lower() == 'reread on':
                    settings["reread"] = True
                    cl.sendMessage(to, "查詢收回開啟")
                elif text.lower() == 'reread off':
                    settings["reread"] = False
                    cl.sendMessage(to, "查詢收回關閉")
                elif text.lower() == '保護開':
                    if msg.toType ==2:
                        G = cl.getGroup(msg.to)
                        settings["protect"][G.id] = True
                        settings["qrprotect"][G.id] = True
                        cl.sendMessage(to, "所有保護開")
                        cl.sendMessage(to, "")
                elif text.lower() == '保護關':
                    if msg.toType ==2:
                        G = cl.getGroup(msg.to)
                        try:
                            del settings["protect"][G.id]
                            cl.sendMessage(to, "所有保護關")
                        except:
                            pass
                        try:
                            del settings["qrprotect"][G.id]
                            cl.sendMessage(to, "")
                        except:
                            pass			
                elif text.lower() == '網址':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = cl.reissueGroupTicket(to)
                            cl.sendMessage(to, "[ 群組網址 ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            cl.sendMessage(to, "群組網址未開啟，請用Ourl先開啟".format(str(settings["keyCommand"])))
                elif text.lower() == '開啟網址':
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            cl.sendMessage(to, "群組網址已開啟")
                        else:
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                            cl.sendMessage(to, "成功開啟群組網址")
                elif text.lower() == '關閉網址':
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == True:
                            cl.sendMessage(to, "群組網址已關閉")
                        else:
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                            cl.sendMessage(to, "成功關閉群組網址")

                elif ("Say " in msg.text):
                    x = text.split(' ',2)
                    c = int(x[2])
                    for c in range(c):
                        cl.sendMessage(to,x[1])
                elif msg.text.lower().startswith("tag "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    x = text.split(' ',2)
                    c = int(x[2])
                    for c in range(c):
                        sendMessageWithMention(to, inkey)
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    cl.sendChatChecked(to, msg_id)
                    kicker01.sendChatChecked(to, msg_id)
                    kicker02.sendChatChecked(to, msg_id)
                    kicker03.sendChatChecked(to, msg_id)
                    kicker04.sendChatChecked(to, msg_id)
                    kicker05.sendChatChecked(to, msg_id)
                    kicker06.sendChatChecked(to, msg_id)
                    kicker07.sendChatChecked(to, msg_id)
                    kicker08.sendChatChecked(to, msg_id)
                    kicker09.sendChatChecked(to, msg_id)
                    kicker10.sendChatChecked(to, msg_id)
                    kicker11.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if msg.contentType == 0 and sender not in clMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if clMID in mention["M"]:
                                if settings["detectMention"] == True:
                                    contact = cl.getContact(sender)
                                    sendMessageWithMention(to, contact.mid)
                                    cl.sendMessage(to, "有事找老爺")
                                break
            try:
                if settings["reread"] == True:
                    if msg.toType == 0:
                        cl.log("[%s]"%(msg._from)+msg.text)
                    else:
                        cl.log("[%s]"%(msg.to)+msg.text)
                    if msg.contentType == 0:
                        msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 65:
            try:
                at = op.param1
                msg_id = op.param2
                if at not in settings["reread"]:
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"] not in bl:
                            cl.sendMessage(at,"[收回訊息者]\n%s\n[訊息內容]\n%s"%(cl.getContact(msg_dict[msg_id]["from"]).displayName,msg_dict[msg_id]["text"]))
                            print ["收回訊息"]
                        del msg_dict[msg_id]
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 55:
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n[•]" + Name
                        wait2['ROM'][op.param1][op.param2] = "[•]" + Name
                else:
                    pass
            except:
                pass
    except Exception as error:
        logError(error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
