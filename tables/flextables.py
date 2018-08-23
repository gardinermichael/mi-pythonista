# Pythonista Forum - @Phuket2
import ui

class MyClass(ui.View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_view()
        
    def make_view(self):
        num_tables = 4
        for i in range(0, num_tables):
            tbl = ui.TableView(name=str(i))
            tbl.width = self.width / num_tables
            tbl.height = self.height
            tbl.x = tbl.width * i
            tbl.data_source = ui.ListDataSource(items=range(40))
            tbl.flex = 'tlwhbr'
            self.add_subview(tbl)
            
            

if __name__ == '__main__':
    w, h = 600, 800
    f = (0, 0, w, h)
    style = 'sheet'
    
    mc = MyClass(frame=f, bg_color='white', name='Tables')
    mc.present(style=style, animated=False)