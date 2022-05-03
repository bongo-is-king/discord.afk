import requests
import os

class Idle:
      API = 'https://discord.com/api/v9'
      API

      class Headers:
            Token = "Authorization"
            Token

      class Data:
            Settings = 'users/@me/settings'
     
class Idler:
      def __init__(self, token = ""):
            
            self.token = token
            self.token

      def change_status(
          self,
          status = ""
      ):
          if status == "":
             status
          else:
             requests.patch(
                      '%s/%s' % (
                            Idle.API,
                            Idle.Data.Settings,
                      ), headers = {
                                 Idle.Headers.Token: self.token
                         }, json = {
                                 'custom_status': {
                                                'text' : status
                                 }
                         }
             )
