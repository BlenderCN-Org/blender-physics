import bpy,os

from ..animate import load_mesh

class AnimatePhysika(bpy.types.Operator):
    bl_idname = "physika_operators.animate"
    bl_label = "Animate Physika Simulation"
    bl_description = "Display Physika Simulation Results"
    bl_options = {'REGISTER'}

    def execute(self, context):
        """ 10 need to be changed to num_frames"""
        # for frame_id in range(10):
        #     print(frame_id)
        mesh_loader = load_mesh.MeshLoader();
        mesh_loader.import_frame_mesh(0)

        return {"FINISHED"}


def register():
    bpy.utils.register_class(AnimatePhysika)

def unregister():
    bpy.utils.unregister_class(AnimatePhysika)

