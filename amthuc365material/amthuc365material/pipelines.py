# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

class Amthuc365MaterialPipeline(object):
    def __init__(self):
    # sua ten database
        self.conn=MySQLdb.connect(user='root',passwd='cobala15111994',db='amthuc365',host='127.0.0.1',charset="utf8",use_unicode='True')
        self.cursor=self.conn.cursor()

    def process_item(self, item,   spider):
        if (spider.name == 'getlink2'):
            try:
                # sua lai lenh insert cho phu hop voi database
                sql = """INSERT INTO dish_material(link) VALUES (\'%s\')""" %(''.join(dishes(link)).decode('utf-8'))
                self.cursor.execute(sql)
                self.conn.commit()
            except MySQLdb.Error, e:
                print ("Error %s" % e.args[1])
            return item

        elif (spider.name =='materialparse'):
            #line = json.dumps(dict(item)).decode('unicode-escape').encode('utf-8') + "\n"
            #self.file.write(line)
            try:
            	# sua lenh update
                self.cursor.execute("UPDATE dish_material SET material = %s, value = %s, type = %s WHERE link = %s",(''.join(item['material']), ''.join(item['value']), ''.join(item['mytype']),''.join(item['link'])))
                self.conn.commit()

            except MySQLdb.Error, e:
                print("Error %s" % e.args[1])
            return item