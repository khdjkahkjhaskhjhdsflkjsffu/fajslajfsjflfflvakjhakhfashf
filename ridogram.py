import modules.client, modules.afoot, modules.selfdestruct, modules.details, modules.bombing, modules.translate, modules.wikipedia, modules.accountlimit, modules.covidinformation, modules.userhistory, modules.iptrace, modules.generatepassword, modules.removemessage, modules.goodmorning, modules.goodafternoon, modules.goodevening, modules.goodnight, modules.telegraph, modules.removealldp, modules.imageaction, modules.removeallmessages, modules.removemessagesforcefully, modules.ban, modules.kick, modules.banall, modules.kickall, modules.calculator, modules.whois, modules.hosthunter, modules.useraccountupdate, modules.texttospeech, modules.secretmessage, modules.phonenumbertrace, modules.restoremessage, modules.ping, modules.emailvalidator, modules.worldclock, modules.urlshortener, modules.qrcode, modules.usernamevalidation, modules.imagetopdf, modules.currencyinformation, modules.googlesearch, modules.webpagescreenshot, modules.zipcodeinformation, modules.tvshowinformation, modules.quotly, modules.dictionary, modules.generatedata, modules.carbon, modules.creditcardchecker, modules.speedtest, modules.updater

client = modules.client.client

with client as ridogram:
    ridogram.add_event_handler(modules.afoot.runafoot)

with client as ridogram:
    ridogram.add_event_handler(modules.selfdestruct.runsdmd)

with client as ridogram:
    ridogram.add_event_handler(modules.details.rundls)

with client as ridogram:
    ridogram.add_event_handler(modules.bombing.runbomb)

with client as ridogram:
    ridogram.add_event_handler(modules.translate.runtr)

with client as ridogram:
    ridogram.add_event_handler(modules.wikipedia.runwiki)

with client as ridogram:
    ridogram.add_event_handler(modules.accountlimit.runacsc)

with client as ridogram:
    ridogram.add_event_handler(modules.covidinformation.runcovid)

with client as ridogram:
    ridogram.add_event_handler(modules.userhistory.runuh)

with client as ridogram:
    ridogram.add_event_handler(modules.iptrace.runiptrace)

with client as ridogram:
    ridogram.add_event_handler(modules.generatepassword.rungpwd)

with client as ridogram:
    ridogram.add_event_handler(modules.removemessage.runrm)

with client as ridogram:
    ridogram.add_event_handler(modules.goodmorning.rungdm)

with client as ridogram:
    ridogram.add_event_handler(modules.goodafternoon.rungda)

with client as ridogram:
    ridogram.add_event_handler(modules.goodevening.rungde)

with client as ridogram:
    ridogram.add_event_handler(modules.goodnight.rungdn)

with client as ridogram:
    ridogram.add_event_handler(modules.telegraph.runtgu)

with client as ridogram:
    ridogram.add_event_handler(modules.removealldp.runrmdps)

with client as ridogram:
    ridogram.add_event_handler(modules.imageaction.runia)

with client as ridogram:
    ridogram.add_event_handler(modules.removeallmessages.runrma)

with client as ridogram:
    ridogram.add_event_handler(modules.removemessagesforcefully.runrmf)

with client as ridogram:
    ridogram.add_event_handler(modules.ban.runban)

with client as ridogram:
    ridogram.add_event_handler(modules.kick.runkick)

with client as ridogram:
    ridogram.add_event_handler(modules.banall.runfba)

with client as ridogram:
    ridogram.add_event_handler(modules.kickall.runfka)

with client as ridogram:
    ridogram.add_event_handler(modules.calculator.runccr)

with client as ridogram:
    ridogram.add_event_handler(modules.whois.runwhois)

with client as ridogram:
    ridogram.add_event_handler(modules.hosthunter.runhh)

with client as ridogram:
    ridogram.add_event_handler(modules.useraccountupdate.runuau)

with client as ridogram:
    ridogram.add_event_handler(modules.texttospeech.runtts)

with client as ridogram:
    ridogram.add_event_handler(modules.secretmessage.runb64)

with client as ridogram:
    ridogram.add_event_handler(modules.phonenumbertrace.runpntrace)

with client as ridogram:
    ridogram.add_event_handler(modules.restoremessage.runrgm)

with client as ridogram:
    ridogram.add_event_handler(modules.ping.runping)

with client as ridogram:
    ridogram.add_event_handler(modules.emailvalidator.runev)

with client as ridogram:
    ridogram.add_event_handler(modules.worldclock.runwc)

with client as ridogram:
    ridogram.add_event_handler(modules.urlshortener.runus)

with client as ridogram:
    ridogram.add_event_handler(modules.qrcode.runqrc)

with client as ridogram:
    ridogram.add_event_handler(modules.usernamevalidation.runuv)

with client as ridogram:
    ridogram.add_event_handler(modules.imagetopdf.runitp)

with client as ridogram:
    ridogram.add_event_handler(modules.currencyinformation.runci)

with client as ridogram:
    ridogram.add_event_handler(modules.googlesearch.rungs)

with client as ridogram:
    ridogram.add_event_handler(modules.webpagescreenshot.runwps)

with client as ridogram:
    ridogram.add_event_handler(modules.zipcodeinformation.runzci)

with client as ridogram:
    ridogram.add_event_handler(modules.tvshowinformation.runtvsi)

with client as ridogram:
    ridogram.add_event_handler(modules.quotly.runq)

with client as ridogram:
    ridogram.add_event_handler(modules.dictionary.runwm)

with client as ridogram:
    ridogram.add_event_handler(modules.generatedata.runfd)

with client as ridogram:
    ridogram.add_event_handler(modules.carbon.runtti)

with client as ridogram:
    ridogram.add_event_handler(modules.creditcardchecker.runn)

with client as ridogram:
    ridogram.add_event_handler(modules.speedtest.runst)
    
with client as ridogram:
    ridogram.add_event_handler(modules.updater.runupdate)

client.start()
print("Ridogram Started")
client.run_until_disconnected()
