import os


class CookieService:

    cookies = {}

    @staticmethod
    def checkWholeCookieFromSetCookies(cookieslist):
        sum = 0
        for co in cookieslist:
            if str(co, encoding = "utf8").find('WEE_SID') != -1:
                sum += 1
            elif str(co, encoding = "utf8").find('IS_LOGIN') != -1:
                sum += 1
            elif str(co, encoding = "utf8").find('JSESSIONID') != -1:
                sum += 1
        if sum == 3:
            return True
        else:
            return False

    @staticmethod
    def readCookiesFromList(coolist):
        for co in coolist:
            if str(co, encoding = "utf8").find('WEE_SID') != -1:
                CookieService.cookies['WEE_SID'] = str(co, encoding = "utf8")[8:]
            elif str(co, encoding = "utf8").find('IS_LOGIN') != -1:
                CookieService.cookies['IS_LOGIN'] = str(co, encoding = "utf8")[9:]
            elif str(co, encoding = "utf8").find('JSESSIONID') != -1:
                CookieService.cookies['JSESSIONID'] = str(co, encoding = "utf8")[11:]
