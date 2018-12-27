import bpy
from ..base_state import *
from . import discrete_types

class physika_parameter_ui(physika_base_ui):
    bl_label = 'Parameter'
    physika_state = 'parameter'

    def valid_common_props(self, string):
        return string.startswith('common')
    
    def draw_common_paras(self, context, para_props):
        self.layout.label('Common parameters:')
        box = self.layout.box()
        common_props = list(filter(self.valid_common_props, dir(para_props)))
        for common_prop in common_props:
            box.column().prop(para_props, common_prop)
        
    def draw_specific_paras(self, context, para_props):
        discrete_method = para_props.physika_discrete
        self.layout.label('Special parameters:')
        box = self.layout.box()
        special_props = [prop[0] for prop in eval('discrete_types.' + discrete_method + '_parameter')]
        for special_prop in special_props:
            box.column().prop(eval('para_props.' + discrete_method), special_prop)        
        
    def draw(self, context):
        super(physika_parameter_ui, self).draw(context)

        para_props = context.scene.physika_para
        
        column = self.layout.column()
        column.label("Set Discrete Method")
        row = column.row(align = True)
        row.prop(para_props, 'physika_discrete', expand = True)

        self.draw_common_paras(context, para_props)
        self.draw_specific_paras(context, para_props)        

class physika_parameter_op_previous(physika_base_op_previous):
    physika_state = 'parameter'
    bl_idname = 'physika_parameter_op.previous'

    
class physika_parameter_op_next(physika_base_op_next):
    physika_state = 'parameter'
    bl_idname = 'physika_parameter_op.next'

def register_state():
    state = bpy.data.scenes['Scene'].physika_state_graph.add()
    state.curr = 'parameter'
    state.next = 'simulate'
    state.prev = 'constraint'

from . import set_parameter    
def register():
    set_parameter.register()
    bpy.utils.register_class(physika_parameter_op_previous)
    bpy.utils.register_class(physika_parameter_op_next)
    bpy.utils.register_class(physika_parameter_ui)

def unregister():
    set_parameter.unregister()
    bpy.utils.unregister_class(physika_parameter_op_previous)
    bpy.utils.unregister_class(physika_parameter_op_next)    
    bpy.utils.unregister_class(physika_parameter_ui)