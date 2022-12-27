import logging

import Queryer

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s : %(levelname)s  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                    )


class Inventory(object):
    def __init__(self):
        # self.store = {'name': amount}
        self.store = {'name': 0}
        self.queryer = Queryer.Queryer
        logging.info('��ʼ�����')

    def inbound(self, items):
        """
        items -> list
        """
        for i in items:
            name = list(i.keys())[0]
            logging.info('��ʼΪ{}׷�ӿ��'.format(name))
            if name in self.store:
                self.store[name] += i[name]
                logging.info('{} ���ڿ��У�׷������ {}��׷�Ӻ����� {}'.format(name, i[name], self.store[name]))
            else:
                self.store.update(i)
                logging.info('{} ���ڿ��У�׷�Ӹ���Ʒ������ {}'.format(name, self.store[name]))
        return True

    def outbound(self, items):
        """
        items -> list
        """
        for i in items:
            a = self.queryer()

            a.query_item_craft()
            a.calibration_quantity(a.stuff['craft'])

    def make_queue(self):
        pass

    def history(self):
        pass

    def update(self):
        pass


if __name__ == '__main__':
    test = Inventory()
    test.inbound([{'name': 10}, {'item1': 1}, {'item2': 5}])
