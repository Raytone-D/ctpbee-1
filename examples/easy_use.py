from ctpbee import CtpbeeApi, CtpBee
from ctpbee.constant import *


class JustUse(CtpbeeApi):

    def __init__(self, name):
        super().__init__(name)
        self.instrument_set = set(['rb2001.SHFE'])

    def on_account(self, account: AccountData) -> None:
        pass

    def on_order(self, order: OrderData) -> None:
        pass

    def on_trade(self, trade: TradeData) -> None:
        pass

    def on_position(self, position: PositionData) -> None:
        pass

    def on_tick(self, tick: TickData) -> None:
        print(tick)

    def on_bar(self, bar: BarData) -> None:
        pass
        dict_bar = bar._to_dict()
        self.action.short(bar.high_price, 1, bar)

    def on_contract(self, contract: ContractData):
        if contract.local_symbol in self.instrument_set:
            self.app.subscribe(contract.local_symbol)

    def on_init(self, init: bool):
        pass


if __name__ == '__main__':
    app = CtpBee("test", __name__)
    just_use = JustUse("Hi")

    info = {
        "CONNECT_INFO": {
            "userid": "089131",
            "password": "350888",
            "brokerid": "9999",
            "md_address": "tcp://180.168.146.187:10131",
            "td_address": "tcp://180.168.146.187:10130",
            "product_info": "",
            "appid": "simnow_client_test",
            "auth_code": "0000000000000000",
        },
        "INTERFACE": "ctp",
        "TD_FUNC": True,
        "MD_FUNC": True,
        "XMIN": [3, 5]
    }
    app.config.from_mapping(info)
    app.add_extension(just_use)
    app.start()
