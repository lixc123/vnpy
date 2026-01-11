from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp

# 网关
from vnpy_ctp import CtpGateway

# 应用模块
from vnpy_ctastrategy import CtaStrategyApp
from vnpy_ctabacktester import CtaBacktesterApp
from vnpy_chartwizard import ChartWizardApp
from vnpy_spreadtrading import SpreadTradingApp
from vnpy_datamanager import DataManagerApp
from vnpy_datarecorder import DataRecorderApp
from vnpy_riskmanager import RiskManagerApp
from vnpy_portfoliostrategy import PortfolioStrategyApp
from vnpy_optionmaster import OptionMasterApp
from vnpy_algotrading import AlgoTradingApp
from vnpy_webtrader import WebTraderApp
from vnpy_paperaccount import PaperAccountApp


def main():
    """Start VeighNa Trader"""
    qapp = create_qapp()

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    
    # 添加网关
    main_engine.add_gateway(CtpGateway)
    
    # 添加应用模块
    main_engine.add_app(CtaStrategyApp)          # CTA策略
    main_engine.add_app(CtaBacktesterApp)        # CTA回测
    main_engine.add_app(ChartWizardApp)          # K线图表
    main_engine.add_app(SpreadTradingApp)        # 价差交易
    main_engine.add_app(DataManagerApp)          # 数据管理
    main_engine.add_app(DataRecorderApp)         # 数据录制
    main_engine.add_app(RiskManagerApp)          # 风险管理
    main_engine.add_app(PortfolioStrategyApp)    # 组合策略
    main_engine.add_app(OptionMasterApp)         # 期权交易
    main_engine.add_app(AlgoTradingApp)          # 算法交易
    main_engine.add_app(WebTraderApp)            # Web服务
    main_engine.add_app(PaperAccountApp)         # 模拟交易

    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()


if __name__ == "__main__":
    main()
