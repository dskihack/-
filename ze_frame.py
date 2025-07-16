import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QPushButton, QFileDialog, QTextEdit, QTableWidget,
                             QTableWidgetItem, QTabWidget, QMessageBox,QHeaderView)
from PyQt6.QtCore import Qt
import pandas as pd



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("语音内容提取填表系统")
        self.setGeometry(100, 100, 900, 600)
        
        # 中央部件和主布局
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # 初始化UI
        self.init_ui()
        
        # 存储数据
        self.template_df = None
        self.data_df = None
        self.audio_files = []
        self.recognized_texts = []
        
    def init_ui(self):
        """初始化用户界面"""
        # 创建标签页
        self.tab_widget = QTabWidget()
        self.main_layout.addWidget(self.tab_widget)
        
        # 添加三个标签页
        self.setup_template_tab()
        self.setup_audio_tab()
        self.setup_data_tab()
        self.setup_result_tab()
        
        # 底部按钮
        self.setup_bottom_buttons()
    
    def setup_template_tab(self):
        """设置Excel模板标签页"""
        self.template_tab = QWidget()
        self.tab_widget.addTab(self.template_tab, "1. Excel模板")
        
        layout = QVBoxLayout(self.template_tab)
        
        # 模板文件选择
        self.template_label = QLabel("请选择样例Excel模板文件:")
        layout.addWidget(self.template_label)
        
        self.template_path_edit = QTextEdit()
        self.template_path_edit.setMaximumHeight(30)
        self.template_path_edit.setReadOnly(True)
        layout.addWidget(self.template_path_edit)
        
        btn_layout = QHBoxLayout()
        self.template_browse_btn = QPushButton("浏览...")
        self.template_browse_btn.clicked.connect(self.browse_template)
        btn_layout.addWidget(self.template_browse_btn)
        
        self.parse_template_btn = QPushButton("解析模板")
        self.parse_template_btn.clicked.connect(self.parse_template)
        self.parse_template_btn.setEnabled(False)
        btn_layout.addWidget(self.parse_template_btn)
        
        layout.addLayout(btn_layout)
        
        # 模板预览表格
        self.template_table_label = QLabel("模板预览:")
        layout.addWidget(self.template_table_label)
        
        self.template_table = QTableWidget()
        self.template_table.setAlternatingRowColors(True)
        layout.addWidget(self.template_table)
    
    def setup_audio_tab(self):
        """设置音频处理标签页"""
        self.audio_tab = QWidget()
        self.tab_widget.addTab(self.audio_tab, "2. 音频处理")
        
        layout = QVBoxLayout(self.audio_tab)
        
        # 音频文件选择
        self.audio_label = QLabel("请选择音频文件(可多选):")
        layout.addWidget(self.audio_label)
        
        self.audio_list_edit = QTextEdit()
        self.audio_list_edit.setMaximumHeight(80)
        self.audio_list_edit.setReadOnly(True)
        layout.addWidget(self.audio_list_edit)
        
        btn_layout = QHBoxLayout()
        self.audio_browse_btn = QPushButton("浏览...")
        self.audio_browse_btn.clicked.connect(self.browse_audio)
        btn_layout.addWidget(self.audio_browse_btn)
        
        self.recognize_btn = QPushButton("语音识别")
        self.recognize_btn.clicked.connect(self.recognize_speech)
        self.recognize_btn.setEnabled(False)
        btn_layout.addWidget(self.recognize_btn)
        
        layout.addLayout(btn_layout)
        
        # 识别结果编辑
        self.result_label = QLabel("语音识别结果(可编辑):")
        layout.addWidget(self.result_label)
        
        self.recognized_text_edit = QTextEdit()
        layout.addWidget(self.recognized_text_edit)
        
        # 识别结果列表
        self.recognized_list_label = QLabel("已识别音频列表:")
        layout.addWidget(self.recognized_list_label)
        
        self.recognized_list_table = QTableWidget(0, 2)
        self.recognized_list_table.setHorizontalHeaderLabels(["音频文件", "文本摘要"])
        self.recognized_list_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.recognized_list_table)
    
    def setup_data_tab(self):
        """设置资料表格标签页"""
        self.data_tab = QWidget()
        self.tab_widget.addTab(self.data_tab, "3. 资料表格(可选)")
        
        layout = QVBoxLayout(self.data_tab)
        
        # 资料文件选择
        self.data_label = QLabel("请选择资料Excel文件(可选):")
        layout.addWidget(self.data_label)
        
        self.data_path_edit = QTextEdit()
        self.data_path_edit.setMaximumHeight(30)
        self.data_path_edit.setReadOnly(True)
        layout.addWidget(self.data_path_edit)
        
        btn_layout = QHBoxLayout()
        self.data_browse_btn = QPushButton("浏览...")
        self.data_browse_btn.clicked.connect(self.browse_data)
        btn_layout.addWidget(self.data_browse_btn)
        
        self.load_data_btn = QPushButton("加载资料")
        self.load_data_btn.clicked.connect(self.load_data)
        btn_layout.addWidget(self.load_data_btn)
        
        layout.addLayout(btn_layout)
        
        # 资料表格预览
        self.data_table_label = QLabel("资料表格预览:")
        layout.addWidget(self.data_table_label)
        
        self.data_table = QTableWidget()
        self.data_table.setAlternatingRowColors(True)
        layout.addWidget(self.data_table)
    
    def setup_result_tab(self):
        """设置结果标签页"""
        self.result_tab = QWidget()
        self.tab_widget.addTab(self.result_tab, "4. 结果导出")
        
        layout = QVBoxLayout(self.result_tab)
        
        # 结果表格
        self.final_result_label = QLabel("填充结果预览:")
        layout.addWidget(self.final_result_label)
        
        self.result_table = QTableWidget()
        self.result_table.setAlternatingRowColors(True)
        layout.addWidget(self.result_table)
        
        # 导出按钮
        self.export_btn = QPushButton("导出Excel")
        self.export_btn.clicked.connect(self.export_result)
        self.export_btn.setEnabled(False)
        layout.addWidget(self.export_btn, alignment=Qt.AlignmentFlag.AlignRight)
    
    def setup_bottom_buttons(self):
        """设置底部操作按钮"""
        btn_layout = QHBoxLayout()
        
        self.prev_btn = QPushButton("上一步")
        self.prev_btn.clicked.connect(self.prev_tab)
        btn_layout.addWidget(self.prev_btn)
        
        self.next_btn = QPushButton("下一步")
        self.next_btn.clicked.connect(self.next_tab)
        btn_layout.addWidget(self.next_btn)
        
        self.main_layout.addLayout(btn_layout)
    
    # 以下是各个按钮的槽函数框架
    def browse_template(self):
        """浏览Excel模板文件"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "选择Excel模板文件", "", "Excel文件 (*.xlsx *.xls)"
        )
        if file_path:
            self.template_path_edit.setText(file_path)
            self.parse_template_btn.setEnabled(True)
    
    def parse_template(self):
        """解析Excel模板"""
        try:
            file_path = self.template_path_edit.toPlainText()
            self.template_df = pd.read_excel(file_path)
            
            # 显示表格内容
            self.display_dataframe(self.template_table, self.template_df)
            
            # 启用下一步操作
            self.recognize_btn.setEnabled(True)
            self.next_btn.setEnabled(True)
            
            QMessageBox.information(self, "成功", "模板解析成功!")
        except Exception as e:
            QMessageBox.warning(self, "错误", f"解析模板失败: {str(e)}")
    
    def browse_audio(self):
        """浏览音频文件"""
        files, _ = QFileDialog.getOpenFileNames(
            self, "选择音频文件", "", "音频文件 (*.wav *.mp3 *.aac)"
        )
        if files:
            self.audio_files = files
            self.audio_list_edit.setText("\n".join(files))
            self.recognize_btn.setEnabled(True)
    
    def recognize_speech(self):
        """语音识别"""
        if not self.audio_files:
            QMessageBox.warning(self, "警告", "请先选择音频文件")
            return
        
        # 这里应该调用百度语音识别API
        # 模拟识别结果
        self.recognized_texts = [
            f"这是从音频 {i+1} 识别出的文本内容" for i in range(len(self.audio_files))
        ]
        
        # 显示第一个识别结果用于编辑
        if self.recognized_texts:
            self.recognized_text_edit.setText(self.recognized_texts[0])
        
        # 更新识别列表表格
        self.recognized_list_table.setRowCount(len(self.audio_files))
        for i, (file, text) in enumerate(zip(self.audio_files, self.recognized_texts)):
            self.recognized_list_table.setItem(i, 0, QTableWidgetItem(file.split('/')[-1]))
            self.recognized_list_table.setItem(i, 1, QTableWidgetItem(text[:50] + "..."))
        
        QMessageBox.information(self, "完成", "语音识别完成!")
    
    def browse_data(self):
        """浏览资料Excel文件"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "选择资料Excel文件", "", "Excel文件 (*.xlsx *.xls)"
        )
        if file_path:
            self.data_path_edit.setText(file_path)
    
    def load_data(self):
        """加载资料Excel文件"""
        try:
            file_path = self.data_path_edit.toPlainText()
            if not file_path:
                QMessageBox.warning(self, "警告", "请先选择资料文件")
                return
                
            self.data_df = pd.read_excel(file_path)
            self.display_dataframe(self.data_table, self.data_df)
            QMessageBox.information(self, "成功", "资料加载成功!")
        except Exception as e:
            QMessageBox.warning(self, "错误", f"加载资料失败: {str(e)}")
    
    def export_result(self):
        """导出结果到Excel"""
        if not hasattr(self, 'result_df') or self.result_df.empty:
            QMessageBox.warning(self, "警告", "没有可导出的数据")
            return
            
        file_path, _ = QFileDialog.getSaveFileName(
            self, "保存结果", "", "Excel文件 (*.xlsx)"
        )
        if file_path:
            try:
                self.result_df.to_excel(file_path, index=False)
                QMessageBox.information(self, "成功", f"结果已导出到: {file_path}")
            except Exception as e:
                QMessageBox.warning(self, "错误", f"导出失败: {str(e)}")
    
    def prev_tab(self):
        """切换到上一个标签页"""
        current = self.tab_widget.currentIndex()
        if current > 0:
            self.tab_widget.setCurrentIndex(current - 1)
    
    def next_tab(self):
        """切换到下一个标签页"""
        current = self.tab_widget.currentIndex()
        if current < self.tab_widget.count() - 1:
            self.tab_widget.setCurrentIndex(current + 1)
        else:
            # 如果是最后一页，尝试生成结果
            self.generate_result()
    
    def generate_result(self):
        """生成最终结果"""
        if self.template_df is None or not self.recognized_texts:
            QMessageBox.warning(self, "警告", "请先完成模板解析和语音识别")
            return
            
        try:
            # 这里应该调用大模型处理数据填充
            # 模拟结果 - 创建与模板相同结构的DataFrame
            self.result_df = self.template_df.iloc[0:0].copy()  # 空DataFrame，只有列名
            
            # 为每个识别文本添加一行
            for text in self.recognized_texts:
                new_row = {col: f"{col}数据({text[:10]}...)" for col in self.result_df.columns}
                self.result_df = pd.concat([self.result_df, pd.DataFrame([new_row])], ignore_index=True)
            
            # 显示结果
            self.display_dataframe(self.result_table, self.result_df)
            self.export_btn.setEnabled(True)
            
            QMessageBox.information(self, "完成", "数据填充完成!")
        except Exception as e:
            QMessageBox.warning(self, "错误", f"生成结果失败: {str(e)}")
    
    def display_dataframe(self, table_widget, dataframe):
        """在QTableWidget中显示DataFrame"""
        if dataframe is None:
            return
            
        table_widget.setRowCount(dataframe.shape[0])
        table_widget.setColumnCount(dataframe.shape[1])
        table_widget.setHorizontalHeaderLabels(dataframe.columns)
        
        for row in range(dataframe.shape[0]):
            for col in range(dataframe.shape[1]):
                item = QTableWidgetItem(str(dataframe.iat[row, col]))
                table_widget.setItem(row, col, item)
        
        table_widget.resizeColumnsToContents()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())