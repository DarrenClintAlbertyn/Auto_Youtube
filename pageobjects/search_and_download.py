# -*- coding: utf-8 -*-
u"""
Copyright 2015 Telefónica Investigación y Desarrollo, S.A.U.
This file is part of Toolium.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class SearchingForTrack(PageObject):
    def init_page_elements(self):
        self.searchBar = InputText(By.XPATH, '//div[@id="search-input"]/input')
        self.searchBtn = Button(By.ID, 'search-icon-legacy')
        self.downloadButton = Button(By.XPATH,'//button[text()="Download Video"]')
        

    def open_web_page(self):
        self.driver.get('{}'.format(self.config.get('Test', 'url')))
        return self

    def wait_until_loaded(self):
        self.searchBar.wait_until_visible()
        return self

    def search_and_find_song(self, artistName, songName):
        self.wait_until_loaded()
        sleep(2)
        self.logger.debug("Searching for {}'s named {}".format(artistName, songName))        
        self.artistNameText = artistName
        self.logger.debug("2nd Line Artist Name Text {}".format(self.artistNameText))
        self.songNameText = songName
        self.logger.debug("3nd Line Song Name Text {}".format(self.songNameText))
        self.searchBar.text = self.artistNameText + " " + self.songNameText    
        self.logger.debug("Final Stuff {} {} before Click".format(self.artistNameText, self.songNameText))
        self.searchBtn.click()
        self.logger.debug("After Click {} {}".format(self.artistNameText, self.songNameText))
        self.loop_through_and_click_on_correct_song(artistName)
        #return True

    def loop_through_and_click_on_correct_song(self,artistName):       
        sleep(3)
        self.trackNameText = Text(By.XPATH,'//a[contains(text(),"{}")]'.format(artistName))
        self.downloadLink = self.trackNameText.get_attribute('href')
        self.logger.debug(self.downloadLink)
        self.str = str(self.downloadLink[:15]) + 'magic' + str(self.downloadLink[15:])
        self.logger.debug(self.str)
        return True

    def download_your_song(self):
        self.logger.debug("Opening Web Page {} ".format(self.str))
        self.driver.get('{}'.format(self.str))
        return self

    def loop_through_format(self):
        self.logger.debug("Looping Function before ")
        self.waitForContainer = Text(By.XPATH, '//div[@class="sv-loading container"]')
        self.logger.debug("Found container")
        self.downloadButton.wait_until_visible()
        self.downloadButton.click()
        self.logger.debug("Clicked and waiting")
        self.driver.implicitly_wait(5)
        self.logger.debug("done waiting")
        sleep(2)
        self.switchToMainPage = self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + '1')
        sleep(2)
        self.logger.debug("Tapped CTRL Thrice")
        #self.waitForContainer.wait_until_visible()
        self.formats = self.driver.find_elements(By.XPATH,'//div[@class="sv-download-links"]/ul')
        for items in self.formats:
            self.allFormats = items.find_element(By.XPATH,'/li[text()]')
            print(self.allFormats.text)