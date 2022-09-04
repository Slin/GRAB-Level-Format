#!/bin/python
import json
from generated import level_pb2, types_pb2
import sys

def find_in_dict(dictionary: dict, val: any) -> str:
    # "Borrowed" code from Google I don't understand
    return dict((new_val,new_k) for new_k,new_val in dictionary.items()).get(val)

def main():
    # Throw error if improperly formatted
    if len(sys.argv) < 3:
        print('Missing Arguments! Proper format is:')
        print('python3 ConvertToJSON.py input.level output.json')
        return -1

    # Define shapes
    shapeMapping = {}
    shapeMapping["cube"] = types_pb2.LevelNodeShape.CUBE
    shapeMapping["sphere"] = types_pb2.LevelNodeShape.SPHERE
    shapeMapping["cylinder"] = types_pb2.LevelNodeShape.CYLINDER
    shapeMapping["pyramid"] = types_pb2.LevelNodeShape.PYRAMID
    shapeMapping["prism"] = types_pb2.LevelNodeShape.PRISM

    # Define types
    typeMapping = {}
    typeMapping["default"] = types_pb2.LevelNodeMaterial.DEFAULT
    typeMapping["default_colored"] = types_pb2.LevelNodeMaterial.DEFAULT_COLORED
    typeMapping["grabbable"] = types_pb2.LevelNodeMaterial.GRABBABLE
    typeMapping["grapplable"] = types_pb2.LevelNodeMaterial.GRAPPLABLE
    typeMapping["ice"] = types_pb2.LevelNodeMaterial.ICE
    typeMapping["lava"] = types_pb2.LevelNodeMaterial.LAVA
    typeMapping["grapplable_lava"] = types_pb2.LevelNodeMaterial.GRAPPLABLE_LAVA
    typeMapping["grabbable_crumbling"] = types_pb2.LevelNodeMaterial.GRABBABLE_CRUMBLING

    # Read level from file
    level = level_pb2.Level()
    try:
        with open(sys.argv[1], "rb") as inputFile:
            level.ParseFromString(inputFile.read())
    except FileNotFoundError as err:
        print(sys.argv[1] + " not found!")
        print(err)
        return -1
    
    output = {}
    try:
        # Assign level metadata
        output["title"] = level.title
        output["description"] = level.description
        output["creators"] = level.creators
        output["checkpoints"] = level.maxCheckpointCount

        # Assign start properties
        output["start"] = {}
        output["start"]["position"] = [
                level.levelNodes[0].levelNodeStart.position.x,
                level.levelNodes[0].levelNodeStart.position.y,
                level.levelNodes[0].levelNodeStart.position.z
            ]
        output["start"]["rotation"] = [
            level.levelNodes[0].levelNodeStart.rotation.x,
            level.levelNodes[0].levelNodeStart.rotation.y,
            level.levelNodes[0].levelNodeStart.rotation.z,
            level.levelNodes[0].levelNodeStart.rotation.w
        ]
        output["start"]["radius"] = level.levelNodes[0].levelNodeStart.radius

        # Assign finish properties
        output["finish"] = {}
        output["finish"]["position"] = [
                level.levelNodes[1].levelNodeFinish.position.x,
                level.levelNodes[1].levelNodeFinish.position.y,
                level.levelNodes[1].levelNodeFinish.position.z
            ]
        output["finish"]["radius"] = level.levelNodes[1].levelNodeFinish.radius

        # Assign properties for all other nodes
        output["nodes"] = []
        for node in level.levelNodes[2:]:
            nodeDict = {}
            nodeStatic = node.levelNodeStatic
            if hasattr(nodeDict, 'type'):
                nodeDict["type"] = find_in_dict(typeMapping, nodeStatic.type)
            else:
                nodeDict["type"] = "default"
            if nodeStatic.shape != 0:
                nodeDict["shape"] = find_in_dict(shapeMapping, nodeStatic.shape)
            else:
                continue
            nodeDict["position"] = [
                nodeStatic.position.x,
                nodeStatic.position.y,
                nodeStatic.position.z
            ]
            nodeDict["rotation"] = [
                nodeStatic.rotation.x,
                nodeStatic.rotation.y,
                nodeStatic.rotation.z,
                nodeStatic.rotation.w
            ]
            nodeDict["scale"] = [
                nodeStatic.scale.x,
                nodeStatic.scale.y,
                nodeStatic.scale.z
            ]
            output["nodes"].append(nodeDict)
        
        # Write to file
        with open(sys.argv[2], "w") as outputFile:
            outputFile.write(json.dumps(output))
        
        print("Succesfully coverted a .level with " + str(level.complexity) + " complexity to .json!")

    except AttributeError as err:
        print(".level file improperly formatted!")
        print(err)
        return -1

if __name__ == "__main__":
    main()