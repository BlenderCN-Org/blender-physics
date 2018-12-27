import bpy
from bpy.props import(
    StringProperty,
    CollectionProperty,
    PointerProperty
)
class physika_state_properties(bpy.types.PropertyGroup):
    @classmethod
    def register(cls):
        bpy.types.Scene.physika_state = PointerProperty(
            name = "physika_state",
            type = cls
        )
        cls.state = StringProperty(default = 'constraint')
        
    @classmethod 
    def unregister(cls):
        del bpy.types.Scene.physika_state


class physika_base_state_properties(bpy.types.PropertyGroup):

    curr = StringProperty()
    next = StringProperty()
    prev = StringProperty()
    


class physika_state_graph(bpy.types.PropertyGroup):
    @classmethod
    def register(cls):
        bpy.types.Scene.physika_state_graph = CollectionProperty(type=physika_base_state_properties)
        
    @classmethod
    def unregister(cls):
        del bpy.types.Scene.physika_state_graph


    
def register():
    bpy.utils.register_class(physika_base_state_properties)
    bpy.utils.register_class(physika_state_graph)
    bpy.utils.register_class(physika_state_properties)

def unregister():
    # del bpy.types.Scene.physika_state_graph
    bpy.utils.unregister_class(physika_base_state_properties)
    bpy.utils.unregister_class(physika_state_graph)
    bpy.utils.unregister_class(physika_state_properties)

