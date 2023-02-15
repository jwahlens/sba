import math

class sba_recipe:

    def __init__(self, name, builder="", rate=0.0, inputs=dict(), byproducts=dict(), is_resource=False):
        self.name        = name
        self.builder     = builder
        self.rate        = rate
        self.inputs      = inputs
        self.byproducts  = byproducts
        self.is_resource = is_resource

class sba_product_list:

    def __init__(self, alternate_recipes=[], stop_points=[]):
        self.alternate_recipes = set([item.lower() for item in alternate_recipes])
        self.stop_points       = set([item.lower() for item in stop_points])
        self.products          = dict()
        self.intermediates     = dict()
        self.recipes           = dict()
        self.byproducts        = dict()
        self.resources         = dict()

        bauxite      = sba_recipe("Bauxite",      is_resource=True)
        self.recipes["bauxite"] = bauxite
        caterium_ore = sba_recipe("Caterium Ore", is_resource=True)
        self.recipes["caterium ore"] = caterium_ore
        coal         = sba_recipe("Coal",         is_resource=True)
        copper_ore   = sba_recipe("Copper Ore",   is_resource=True)
        crude_oil    = sba_recipe("Crude Oil",    is_resource=True)
        iron_ore     = sba_recipe("Iron Ore",     is_resource=True)
        limestone    = sba_recipe("Limestone",    is_resource=True)
        nitrogen_gas = sba_recipe("Nitrogen Gas", is_resource=True)
        raw_quartz   = sba_recipe("Raw Quartz",   is_resource=True)
        sulfur       = sba_recipe("Sulfur",       is_resource=True)
        uranium      = sba_recipe("Uranium",      is_resource=True)
        water        = sba_recipe("Water",        is_resource=True)
        self.recipes["coal"] = coal
        self.recipes["copper ore"] = copper_ore
        self.recipes["crude oil"] = crude_oil
        self.recipes["iron ore"] = iron_ore
        self.recipes["limestone"] = limestone
        self.recipes["nitrogen gas"] = nitrogen_gas
        self.recipes["raw quartz"] = raw_quartz
        self.recipes["sulfur"] = sulfur
        self.recipes["uranium"] = uranium
        self.recipes["water"] = water


        coated_cable = sba_recipe("Coated Cable",
                builder="Refineries",
                rate=67.5,
                inputs={"wire":37.5,
                        "heavy oil residue":15.0})
        insulated_cable = sba_recipe("Insulated Cable",
                builder = "Assemblers",
                rate = 100.0,
                inputs = {"wire":45.0,
                          "rubber":30.0})
        quickwire_cable = sba_recipe("Quickwire Cable",
                builder = "Assemblers",
                rate = 27.5,
                inputs = {"quickwire":7.5,
                          "rubber":5.5})
        cable = sba_recipe("Cable",
                builder = "Constructors",
                rate = 60.0,
                inputs = {"wire":60.0})

        if "coated cable" in self.alternate_recipes:
            self.recipes["cable"] = coated_cable
        elif "insulated cable" in self.alternate_recipes:
            self.recipes["cable"] = insulated_cable
        elif "quickwire cable" in self.alternate_recipes:
            self.recipes["cable"] = quickwire_cable
        else:
            self.recipes["cable"] = cable


        rubber_concrete = sba_recipe("Rubber Concrete",
                builder = "Assemblers",
                rate = 45.0,
                inputs = {"limestone":50.0,
                          "rubber":10.0})
        wet_concrete = sba_recipe("Wet Concrete",
                builder = "Refineries",
                rate = 80.0,
                inputs = {"limestone":120.0,
                          "water":100.0})
        fine_concrete = sba_recipe("Fine Concrete",
                builder = "Assemblers",
                rate = 25.0,
                inputs = {"silica":7.5,
                          "limestone":30.0})
        concrete = sba_recipe("Concrete",
                builder = "Constructors",
                rate = 15.0,
                inputs = {"limestone":45.0})

        if "rubber concrete" in self.alternate_recipes:
            self.recipes["concrete"] = rubber_concrete
        elif "wet concrete" in self.alternate_recipes:
            self.recipes["concrete"] = wet_concrete
        elif "fine concrete" in self.alternate_recipes:
            self.recipes["concrete"] = fine_concrete
        else:
            self.recipes["concrete"] = concrete


        copper_alloy_ingot = sba_recipe("Copper Alloy Ingot",
                                      builder = "Foundries",
                                      rate = 100.0,
                                      inputs = {"copper ore":50.0,
                                                "iron ore":25.0})
        pure_copper_ingot = sba_recipe("Pure Copper Ingots",
                                      builder = "Refineries",
                                      rate = 37.5,
                                      inputs = {"copper ore": 15.0,
                                                "water":10.0})
        copper_ingot = sba_recipe("Copper Ingots",
                                      builder = "Smelters",
                                      rate = 30.0,
                                      inputs = {"copper ore":30.0})

        if "copper alloy ingot" in self.alternate_recipes:
            self.recipes["copper ingot"] = copper_alloy_ingot
        elif "pure copper ingot" in self.alternate_recipes:
            self.recipes["copper ingot"] = pure_copper_ingot
        else:
            self.recipes["copper ingot"] = copper_ingot


        pure_iron_ingot = sba_recipe("Pure Iron Ingots",
                                    builder = "Refineries",
                                    rate = 65.0,
                                    inputs  = {"iron ore":35.0,
                                               "water": 20.0})
        iron_alloy_ingot = sba_recipe("Iron Alloy Ingots",
                                    builder = "Foundries",
                                    rate = 50.0,
                                    inputs = {"iron ore":20.0,
                                              "copper ore": 20.0})
        iron_ingot = sba_recipe("Iron Ingots",
                                    builder = "Smelters",
                                    rate = 30.0,
                                    inputs = {"iron ore":30.0})

        if "pure iron ingot" in self.alternate_recipes:
            self.recipes["iron ingot"] = pure_iron_ingot
        elif "iron alloy ingot" in self.alternate_recipes:
            self.recipes["iron ingot"] = iron_alloy_ingot
        else:
            self.recipes["iron ingot"] = iron_ingot


        coated_iron_plate = sba_recipe("Coated Iron Plates",
                                    builder = "Assemblers",
                                    rate  = 75.0,
                                    inputs = {"iron ingot":50.0,
                                              "plastic":10.0})
        steel_coated_plate = sba_recipe("Steel Coated Plates",
                                    builder = "Assemblers",
                                    rate  = 45.0,
                                    inputs = {"steel ingot":7.5,
                                              "plastic":5.0})
        iron_plate = sba_recipe("Iron Plates",
                                    builder = "Constructors",
                                    rate = 20.0,
                                    inputs = {"iron ingot":30.0})

        if "coated iron plate" in self.alternate_recipes:
            self.recipes["iron plate"] = coated_iron_plate
        elif "steel coated plate" in self.alternate_recipes:
            self.recipes["iron plate"] = steel_coated_plate
        else:
            self.recipes["iron plate"] = iron_plate


        steel_rod = sba_recipe("Steel Rods",
                                  builder = "Constructors",
                                  rate = 48.0,
                                  inputs = {"steel ingot": 12.0})
        iron_rod = sba_recipe("Iron Rods",
                                  builder = "Constructors",
                                  rate = 15.0,
                                  inputs = {"iron ingot":15.0})

        self.recipes["iron rod"] = steel_rod if "steel rod" in self.alternate_recipes else iron_rod


        adhered_iron_plate = sba_recipe("Adhered Iron Plates",
                                               builder = "Assemblers",
                                               rate = 3.75,
                                               inputs = {"iron plate":11.25,
                                                         "rubber":3.75})
        bolted_iron_plate = sba_recipe("Bolted Iron Plates",
                                               builder = "Assemblers",
                                               rate = 15.0,
                                               inputs = {"iron plate":90.0,
                                                         "screw":250.0})
        stitched_iron_plate = sba_recipe("Stitched Iron Plates",
                                               builder = "Assemblers",
                                               rate = 5.625,
                                               inputs = {"iron plate":18.75,
                                                         "wire":37.5})
        reinforced_iron_plate = sba_recipe("Reinforced Iron Plates",
                                               builder = "Assemblers",
                                               rate  = 5.0,
                                               inputs = {"iron plate":30.0,
                                                         "screw":60.0})

        if "adhered iron plate" in self.alternate_recipes:
            self.recipes["reinforced iron plate"] = adhered_iron_plate
        elif "bolted iron plate" in self.alternate_recipes:
            self.recipes["reinforced iron plate"] = bolted_iron_plate
        elif "stitched iron plate" in self.alternate_recipes:
            self.recipes["reinforced iron plate"] = stitched_iron_plate
        else:
            self.recipes["reinforced iron plate"] = reinforced_iron_plate


        cast_iron_screw = sba_recipe("Cast Iron Screws",
                               builder = "Constructors",
                               rate = 50.0,
                               inputs = {"iron ingot":12.5})
        steel_screw = sba_recipe("Steel Screws",
                               builder = "Constructors",
                               rate = 260.0,
                               inputs = {"steel beam":5.0})
        screw = sba_recipe("Screws",
                               builder = "Constructors",
                               rate = 40.0,
                               inputs = {"iron rod":10.0})

        if "cast iron screw" in self.alternate_recipes:
            self.recipes["screw"] = cast_iron_screw
        elif "steel screw" in self.alternate_recipes:
            self.recipes["screw"] = steel_screw
        else:
            self.recipes["screw"] = screw


        fused_wire = sba_recipe("Fused Wire",
                              builder = "Assemblers",
                              rate = 90.0,
                              inputs = {"copper ingot":12.0,
                                        "caterium ingot":3.0})
        iron_wire = sba_recipe("Iron Wire",
                              builder = "Constructors",
                              rate = 22.5,
                              inputs = {"iron ingot":12.5})
        caterium_wire = sba_recipe("Caterium Wire",
                              builder = "Constructors",
                              rate = 120.0,
                              inputs = {"caterium ingot":15.0})
        wire = sba_recipe("Wire",
                              builder = "Constructors",
                              rate = 30.0,
                              inputs = {"copper ingot":15.0})

        if "fused wire" in self.alternate_recipes:
            self.recipes["wire"] = fused_wire
        elif "iron wire" in self.alternate_recipes:
            self.recipes["wire"] = iron_wire
        elif "caterium wire" in self.alternate_recipes:
            self.recipes["wire"] = caterium_wire
        else:
            self.recipes["wire"] = wire


        steamed_copper_sheet = sba_recipe("Steamed Copper Sheets",
                                      builder = "Refineries",
                                      rate = 22.5,
                                      inputs = {"copper ingot":22.5,
                                                "water":22.5})

        copper_sheet = sba_recipe("Copper Sheets",
                                      builder = "Constructors",
                                      rate = 10.0,
                                      inputs = {"copper ingot":20.0})

        self.recipes["copper sheet"] = steamed_copper_sheet if "steamed copper sheet" in self.alternate_recipes else copper_sheet


        bolted_frame = sba_recipe("Bolted Frames",
                                      builder = "Assemblers",
                                      rate = 5.0,
                                      inputs = {"reinforced iron plate":7.5,
                                                "screw":140.0})
        steeled_frame = sba_recipe("Steeled Frames",
                                       builder = "Assemblers",
                                       rate = 3.0,
                                       inputs = {"reinforced iron plate":2.0,
                                                 "steel pipe":10.0})
        modular_frame = sba_recipe("Modular Frames",
                                       builder = "Assemblers",
                                       rate = 2.0,
                                       inputs = {"reinforced iron plate": 3.0,
                                                 "iron rod":12.0})

        if "bolted frame" in self.alternate_recipes:
            self.recipes["modular frame"] = bolted_frame
        elif "steeled frame" in self.alternate_recipes:
            self.recipes["modular frame"] = steeled_frame
        else:
            self.recipes["modular frame"] = modular_frame


        copper_rotor = sba_recipe("Copper Rotors",
                               builder = "Assemblers",
                               rate = 11.25,
                               inputs = {"copper sheet":22.5,
                                         "screw":195.5})
        steel_rotor = sba_recipe("Steel Rotors",
                               builder = "Assemblers",
                               rate = 5.0,
                               inputs = {"steel pipe":10.0,
                                         "wire":30.0})
        rotor = sba_recipe("Rotors",
                               builder = "Assemblers",
                               rate = 4.0,
                               inputs = {"iron rod":20.0,
                                         "screw":100.0})

        if "copper rotor" in self.alternate_recipes:
            self.recipes["rotor"] = copper_rotor
        elif "steel rotor" in self.alternate_recipes:
            self.recipes["rotor"] = steel_rotor
        else:
            self.recipes["rotor"] = rotor


        plastic_smart_plating = sba_recipe("Plastic Smart Plating",
                                   builder = "Manufacturers",
                                   rate = 5.0,
                                   inputs = {"reinforced iron plate":2.5,
                                             "rotor":2.5,
                                             "plastic":7.5})
        smart_plating = sba_recipe("Smart Plating",
                                   builder = "Assemblers",
                                   rate = 2.0,
                                   inputs = {"reinforced iron plate":2.0,
                                             "rotor":2.0})

        self.recipes["smart plating"] = plastic_smart_plating if "plastic smart plating" in self.alternate_recipes else smart_plating


        steel_beam = sba_recipe("Steel Beams",
                                                builder = "Constructors",
                                                rate = 15.0,
                                inputs = {"steel ingot":60.0})

        self.recipes["steel beam"] = steel_beam


        quickwire_stator = sba_recipe("Quickwire Stators",
                                builder = "Assemblers",
                                rate = 8.0,
                                inputs = {"steel pipe":16,
                                          "quickwire":60.0})
        stator = sba_recipe("Stators",
                                builder = "Assemblers",
                                rate = 5.0,
                                inputs = {"steel pipe":15.0,
                                          "wire":40.0})

        self.recipes["stator"] = quickwire_stator if "quickwire stator" in self.alternate_recipes else stator


        #motor
        rigour_motor = sba_recipe("Rigour Motors",
                               builder = "Manufacturers",
                               rate = 7.5,
                               inputs = {"rotor":3.75,
                                         "stator":3.75,
                                         "crystal oscillator":1.25})
        electric_motor = sba_recipe("Electric Motors",
                               builder = "Assemblers",
                               rate = 7.5,
                               inputs = {"electromagnetic control rod":3.75,
                                         "rotor":7.5})
        motor = sba_recipe("Motors",
                               builder = "Assemblers",
                               rate = 5.0,
                               inputs = {"rotor":10.0,
                                         "stator":10.0})

        if "rigour motor" in self.alternate_recipes:
            self.recipes["motor"] = rigour_motor
        elif "electric motor" in self.alternate_recipes:
            self.recipes["motor"] = electric_motor
        else:
            self.recipes["motor"] = motor


        #automated wiring
        automated_speed_wiring = sba_recipe("Automated Speed Wiring",
                                   builder = "Manufacturers",
                                   rate = 7.5,
                                   inputs = {"stator":3.75,
                                             "wire":75.0,
                                             "high-speed connector":1.875})
        automated_wiring = sba_recipe("Automated Wiring",
                                          builder = "Assemblers",
                                          rate = 2.5,
                                          inputs = {"stator":2.5,
                                                    "cable":50.0})

        self.recipes["automated wiring"] = automated_speed_wiring if "automated speed wiring" in self.alternate_recipes else automated_wiring


        #encased industrial beam
        encased_industrial_pipe = sba_recipe("Encased Industrial Pipe",
                                                 builder = "Assemblers",
                                                 rate = 4.0,
                                                 inputs = {"steel pipe":28.0,
                                                           "concrete":20.0})
        encased_industrial_beam = sba_recipe("Encased Industrial Beams",
                                                 builder = "Assemblers",
                                                 rate = 6.0,
                                                 inputs = {"steel beam":24.0,
                                                           "concrete":30.0})

        self.recipes["encased industrial beam"] = encased_industrial_pipe if "encased industrial pipe" in self.alternate_recipes else encased_industrial_beam


        #heavy modular frame
        heavy_flexible_frame = sba_recipe("Heavy Flexible Frames",
             builder = "Manufacturers",
             rate = 3.75,
             inputs = {"modular frame":18.75,
                       "encased industrial beam":11.25,
                       "rubber":75.0,
                       "screw":390.0})
        heavy_encased_frame = sba_recipe("Heavy Encased Frames",
            builder = "Manufacturers",
            rate = 2.8125,
            inputs = {"modular frame":7.5,
                      "encased industrial beam":9.375,
                      "steel pipe":33.75,
                      "concrete":20.625})
        heavy_modular_frame = sba_recipe("Heavy Modular Frame",
            builder = "Manufacturers",
            rate = 2.0,
            inputs = {"modular frame":10.0,
                      "steel pipe":30.0,
                      "encased industrial beam":10.0,
                      "screw":200.0})

        if "heavy flexible frame" in self.alternate_recipes:
            self.recipes["heavy modular frame"] = heavy_flexible_frame
        elif "heavy encased frame" in self.alternate_recipes:
            self.recipes["heavy modular frame"] = heavy_encased_frame
        else:
            self.recipes["heavy modular frame"] = heavy_modular_frame


        #versatile framework
        flexible_framework = sba_recipe("Flexible Framework",
                                     builder = "Manufacturers",
                                     rate = 7.5,
                                     inputs = {"modular frame":3.75,
                                               "steel beam":22.5,
                                               "rubber":30.0})
        versatile_framework = sba_recipe("Versatile Framework",
                                     builder = "Assemblers",
                                     rate = 5.0,
                                     inputs = {"modular frame":2.5,
                                               "steel beam":30.0})

        self.recipes["versatile framework"] = flexible_framework if "flexible framework" in self.alternate_recipes else versatile_framework


        #steel pipe
        steel_pipe = sba_recipe("Steel Pipe",
                                               builder = "Constructors",
                                               rate = 20.0,
                                               inputs = {"steel ingot":30.0})

        self.recipes["steel pipe"] = steel_pipe


        #steel ingot
        coke_steel_ingot = sba_recipe("Coke Steel Ingots",
                                     builder = "Foundries",
                                     rate = 100.0,
                                     inputs = {"iron ore":75.0,
                                               "petrolium coke":75.0})
        compacted_steel_ingot = sba_recipe("Compacted Steel Ingots",
                                     builder = "Foundries",
                                     rate = 37.5,
                                     inputs = {"iron ore":22.5,
                                               "compacted coal":11.25})
        solid_steel_ingot = sba_recipe("Solid Steel Ingots",
                                     builder = "Foundries",
                                     rate = 60.0,
                                     inputs = {"iron ingot":40.0,
                                               "coal":40.0})
        steel_ingot = sba_recipe("Steel Ingots",
                                     builder = "Foundries",
                                     rate = 45.0,
                                     inputs = {"iron ore":45.0,
                                               "coal":45.0})

        if "coke steel ingot" in self.alternate_recipes:
            self.recipes["steel ingot"] = coke_steel_ingot
        elif "compacted steel ingot" in self.alternate_recipes:
            self.recipes["steel ingot"] = compacted_steel_ingot
        else:
            self.recipes["steel ingot"] = steel_ingot


        #packaged sulfuric acid
        packaged_sulfuric_acid = sba_recipe("Packaged Sulfuric Acid",
                                               builder = "Packagers",
                                               rate = 40.0,
                                               inputs = {"sulfuric acid":40.0,
                                                         "empty canister":40.0})

        self.recipes["packaged sulfuric acid"] = packaged_sulfuric_acid


        #sulfuric acid
        unpackaged_sulfuric_acid = sba_recipe("Unpackage Sulfuric Acid",
                                       builder = "Packagers",
                                       rate = 60.0,
                                       inputs = {"packaged sulfuric acid":60.0},
                                       byproducts = {"empty canister":60.0})
        sulfuric_acid = sba_recipe("Sulfuric Acid",
                                       builder = "Refineries",
                                       rate = 50.0,
                                       inputs = {"sulfur":50.0,
                                                 "water":50.0})

        self.recipes["sulfuric acid"] = sulfuric_acid


        #radio control unit
        radio_control_unit = sba_recipe("Radio Control Units",
                                        builder = "Manufacturers",
                                        rate = 2.5,
                                        inputs = {"aluminum casing":40.0,
                                                  "crystal oscillator":1.25,
                                                  "computer":1.25})
        radio_control_system = sba_recipe("Radio Control Systems",
                                          builder = "Manufacturers",
                                          rate = 4.5,
                                          inputs = {"crystal oscillator":1.5,
                                                    "circut board":15.0,
                                                    "aluminum casing":90.0,
                                                    "rubber":45.0})
        radio_connection_unit = sba_recipe("Radio Connection Units",
                                           builder = "Manufacturers",
                                           rate = 3.75,
                                           inputs = {"heat sink":15.0,
                                                     "high speed connector":7.5,
                                                     "quartz crystal": 45.0})

        if "radio control system" in self.alternate_recipes:
            self.recipes["radio control unit"] = radio_control_system
        elif "radio connection unit" in self.alternate_recipes:
            self.recipes["radio control system"] = radio_connection_unit
        else:
            self.recipes["radio control unit"] = radio_control_unit


        #battery
        battery = sba_recipe("Batteries",
                             builder = "Blenders",
                             rate = 20.0,
                             inputs = {"sulfuric acid":50.0,
                                       "alumina solution":40.0,
                                       "aluminum casing":20.0},
                             byproducts = {"water":30.0})
        classic_battery = sba_recipe("Classic Batteries",
                                     builder = "Manufacturers",
                                     rate = 30.0,
                                     inputs = {"sulfur":45.0,
                                               "alclad aluminum sheet":52.5,
                                               "plastic":60.0,
                                               "wire":90.0})

        self.recipes["battery"] = classic_battery if "classic battery" in self.alternate_recipes else battery


        #assembly director system
        assembly_director_system = sba_recipe("Assembly Director Systems",
                                          builder = "Assemblers",
                                          rate = 0.75,
                                          inputs = {"adaptive control unit":1.5,
                                                    "supercomputer":0.75})

        self.recipes["assembly director system"] = assembly_director_system


        #aluminum scrap
        aluminum_scrap = sba_recipe("Aluminum Scrap",
                                    builder = "Refineries",
                                    rate = 360.0,
                                    inputs = {"alumina solution":240.0,
                                              "coal":120.0},
                                    byproducts = {"water":120.0})
        electrode_aluminum_scrap = sba_recipe("Electrode-Aluminum Scrap",
                                              builder = "Refineries",
                                              rate = 300.0,
                                              inputs = {"alumina solution":180.0,
                                                        "petrolium coke":60.0},
                                              byproducts = {"water":105.0})
        instant_scrap = sba_recipe("Instant Scrap",
                                   builder = "Blenders",
                                   rate = 300.0,
                                   inputs = {"bauxite":300.0,
                                             "coal":100.0,
                                             "sulfuric acid":50.0,
                                             "water":60.0},
                                   byproducts = {"water":50.0})

        if "electrode-aluminum scrap" in self.alternate_recipes:
            self.recipes["aluminum scrap"] = electrode_aluminum_scrap
        elif "instant scrap" in self.alternate_recipes:
            self.recipes["aluminum scrap"] = instant_scrap
        else:
            self.recipes["aluminum scrap"] = aluminum_scrap


        #aluminum ingot
        aluminum_ingot = sba_recipe("Aluminum Ingots",
                                    builder = "Foundries",
                                    rate = 60.0,
                                    inputs = {"aluminum scrap":90.0,
                                              "silica":75.0})
        pure_aluminum_ingot = sba_recipe("Pure Aluminum Ingots",
                                         builder = "Smelters",
                                         rate = 30.0,
                                         inputs = {"aluminum scrap":60.0})

        self.recipes["aluminum ingot"] = pure_aluminum_ingot if "pure aluminum ingot" in self.alternate_recipes else aluminum_ingot


        #alclad aluminum sheet
        alclad_aluminum_sheet = sba_recipe("Alclad Aluminum Sheet",
                                               builder = "Assemblers",
                                               rate = 30.0,
                                               inputs = {"aluminum ingot":30.0,
                                                         "copper ingot":10.0})

        self.recipes["alclad aluminum sheet"] = alclad_aluminum_sheet


        #aluminum casing
        aluminum_casing = sba_recipe("Aluminum Casing",
                                     builder = "Constructors",
                                     rate = 60.0,
                                     inputs = {"aluminum ingot":90.0})
        alclad_casing = sba_recipe("Alclad Casing",
                                   builder = "Assemblers",
                                   rate = 112.5,
                                   inputs = {"aluminum ingot": 150.0,
                                             "copper ingot":75.0})

        self.recipes["aluminum casing"] = alclad_casing if "alclad casing" in self.alternate_recipes else aluminum_casing


        #packaged alumina solution
        packaged_alumina_solution = sba_recipe("Packaged Alumina Solution",
                                               builder = "Packagers",
                                               rate = 120.0,
                                               inputs = {"alumina solution":120.0,
                                                         "empty canister":120.0})

        self.recipes["packaged alumina solution"] = packaged_alumina_solution


        #alumina Solution
        alumina_solution = sba_recipe("Alumina Solution",
                                      builder = "Refineries",
                                      rate = 120.0,
                                      inputs = {"bauxite":120.0,
                                                "water":120.0},
                                      byproducts = {"silica":50.0})
        unpackaged_alumina_solution = sba_recipe("Unpackaged Alumina Solution",
                                                 builder = "Packagers",
                                                 rate = 120.0,
                                                 inputs = {"packaged alumina solution":120.0},
                                                 byproducts = {"empty canister":120.0})
        sloppy_alumina = sba_recipe("Sloppy Alumina",
                                    builder = "Refineries",
                                    rate = 240.0,
                                    inputs = {"bauxite":200.0,
                                              "water":200.0})

        if "sloppy alumina" in self.alternate_recipes:
            self.recipes["alumina solution"] = sloppy_alumina
        else:
            self.recipes["alumina solution"] = alumina_solution


        #packaged oil
        packaged_oil = sba_recipe("Packaged Oil",
                                  builder = "Packagers",
                                  rate = 30.0,
                                  inputs = {"crude oil":30.0,
                                            "empty canister":30.0})

        self.recipes["packaged oil"] = packaged_oil


        #packaged nitrogen gas
        packaged_nitrogen_gas = sba_recipe("Packaged Nitrogen Gas",
                                           builder = "Packagers",
                                           rate = 60.0,
                                           inputs = {"notrogen gas":240.0,
                                                     "empty fluid tank":60.0})

        self.recipes["packaged nitrogen gas"] = packaged_nitrogen_gas


        #packaged water
        packaged_water = sba_recipe("Packaged Water",
                                    builder = "Packagers",
                                    rate = 60.0,
                                    inputs = {"water":60.0,
                                              "empty canister":60.0})

        self.recipes["packaged water"] = packaged_water


        #petrolium coke
        petrolium_coke = sba_recipe("Petrolium Coke",
                                    builder = "Refineries",
                                    rate = 120.0,
                                    inputs = {"heavy oil residue":40.0})

        self.recipes["petrolium coke"] = petrolium_coke


        #polymer resin
        polymer_resin = sba_recipe("Polymer Resin",is_resource=True)
        self.recipes["polymer resin"] = polymer_resin


        #rubber
        rubber = sba_recipe("Rubber",
                            builder = "Refineries",
                            rate = 20.0,
                            inputs = {"crude oil":30.0},
                            byproducts = {"heavy oil residue":20.0})
        residual_rubber = sba_recipe("Residual Rubber",
                                     builder = "Refineries",
                                     rate = 20.0,
                                     inputs = {"polymer resin":40.0,
                                               "water":40.0})
        recycled_rubber = sba_recipe("Recycled Rubber",
                                     builder = "Refineries",
                                     rate  = 60.0,
                                     inputs = {"plastic":30.0,
                                               "fuel":30.0})

        if "residual rubber" in self.alternate_recipes:
            self.recipes["rubber"] = residual_rubber
        elif "recycled rubber" in self.alternate_recipes:
            self.recipes["rubber"] = recycled_rubber
        else:
            self.recipes["rubber"] = rubber


        #modular engine
        modular_engine = sba_recipe("Modular Engines",
                                    builder = "Manufacturers",
                                    rate = 1.0,
                                    inputs = {"motor":2.0,
                                              "rubber":15.0,
                                              "smart plating":2.0})

        self.recipes["modular engine"] = modular_engine


        #fuel
        fuel = sba_recipe("Fuel",
                          builder = "Refineries",
                          rate = 40.0,
                          inputs = {"crude oil":60.0},
                          byproducts = {"polymer_resin":30.0})
        residual_fuel = sba_recipe("Residual Fuel",
                                   builder = "Refineries",
                                   rate = 40.0,
                                   inputs = {"heavy oil residue":60.0})
        unpackaged_fuel = sba_recipe("Unpackaged Fuel",
                                     builder = "Packagers",
                                     rate = 60.0,
                                     inputs = {"packaged fuel":60.0},
                                     byproducts = {"empty canister":60.0})
        diluted_fuel = sba_recipe("Diluted Fuel",
                                  builder = "Blenders",
                                  rate = 100.0,
                                  inputs = {"heavy oil residue":50.0,
                                            "water":100.0})

        if "residual fuel" in self.alternate_recipes:
            self.recipes["fuel"] = residual_fuel
        elif "diluted fuel" in self.alternate_recipes:
            self.recipes["fuel"] = diluted_fuel
        else:
            self.recipes["fuel"] = fuel


        #packaged Fuel
        packaged_fuel = sba_recipe("Packaged Fuel",
                                   builder = "Packagers",
                                   rate = 40.0,
                                   inputs = {"fuel":40.0,
                                             "empty canister":40.0})
        diluted_packaged_fuel = sba_recipe("Diluted Packaged Fuel",
                                           builder = "Refineries",
                                           rate = 60.0,
                                           inputs = {"heavy oil residue":30.0,
                                                     "packaged water":60.0})

        self.recipes["packaged fuel"] = diluted_packaged_fuel if "diluted packaged fuel" in self.alternate_recipes else packaged_fuel


        #packaged heavy oil residue
        packaged_heavy_oil_residue = sba_recipe("Packaged Heavy Oil Residue",
                                                builder = "Packagers",
                                                rate = 30.0,
                                                inputs = {"heavy oil residue":30.0,
                                                          "empty canister":30.0})

        self.recipes["packaged heavy oil residue"] = packaged_heavy_oil_residue


        #heavy oil residue
        unpackaged_heavy_oil_residue = sba_recipe("Unpackaged Heavy Oil Residue",
                                                  builder = "Packagers",
                                                  rate = 20.0,
                                                  inputs = {"packaged heavy oil residue":20.0},
                                                  byproducts = {"empty canister":20.0})

        heavy_oil_residue = sba_recipe("Heavy Oil Residue", is_resource=True)

        self.recipes["heavy oil residue"] = heavy_oil_residue


        #petrolium coke
        petrolium_coke = sba_recipe("Petrolium Coke",
                                    builder = "Refineries",
                                    rate = 120.0,
                                    inputs = {"heavy oil residue":40.0})

        self.recipes["petrolium coke"] = petrolium_coke


        #plastic
        plastic = sba_recipe("Plastic",
                             builder = "Refineries",
                             rate = 20.0,
                             inputs = {"crude oil":30.0},
                             byproducts = {"heavy oil residue":10.0})
        residual_plastic = sba_recipe("Residual Plastic",
                                      builder = "Refineries",
                                      rate = 20.0,
                                      inputs = {"polymer resin":60.0,
                                                "water":20.0})
        recycled_plastic = sba_recipe("Recycled Plastic",
                                      builder = "Refineries",
                                      rate = 60.0,
                                      inputs = {"rubber":30.0,
                                                "fuel":30.0})

        if "residual plastic" in self.alternate_recipes:
            self.recipes["plastic"] = residual_plastic
        elif "recycled plastic" in self.alternate_recipes:
            self.recipes["plastic"] = recycled_plastic
        else:
            self.recipes["plastic"] = plastic


        #empty canister
        empty_canister = sba_recipe("Empty Canisters",
                                    builder = "Constructors",
                                    rate = 60.0,
                                    inputs = {"plastic":30.0})
        steel_canister = sba_recipe("Steel Canisters",
                                    builder = "Constructors",
                                    rate = 40.0,
                                    inputs = {"steel ingot":60.0})
        coated_iron_canister = sba_recipe("Coated Iron Canisters",
                                          builder = "Assemblers",
                                          rate = 60.0,
                                          inputs = {"iron plate":30.0,
                                                    "copper sheet":15.0})

        if "steel canister" in self.alternate_recipes:
            self.recipes["empty canister"] = steel_canister
        elif "coated iron canister" in self.alternate_recipes:
            self.recipes["empty canister"] = coated_iron_canister
        else:
            self.recipes["empty canister"] = empty_canister


        #computer
        computer = sba_recipe("Computer",
                              builder = "Manufacturers",
                              rate = 2.5,
                              inputs = {"circut board":25.0,
                                        "cable":22.5,
                                        "plastic":45.0,
                                        "screw":130.0})
        crystal_computer = sba_recipe("Crystal Computer",
                                      builder = "Assemblers",
                                      rate = 2.8125,
                                      inputs = {"circut board":7.5,
                                                "crystal oscillator":2.8125})
        caterium_computer = sba_recipe("Caterium Computer",
                                       builder = "Manufacturers",
                                       rate = 3.75,
                                       inputs = {"circut board":26.25,
                                                 "quickwire":105.0,
                                                 "rubber":45.0})

        if "crystal computer" in self.alternate_recipes:
            self.recipes["computer"] = crystal_computer
        elif "caterium computer" in self.alternate_recipes:
            self.recipes["computer"] = caterium_computer
        else:
            self.recipes["computer"] = computer


        #circut board
        circut_board = sba_recipe("Circut Board",
                                  builder = "Assemblers",
                                  rate = 7.5,
                                  inputs = {"copper sheet":15.0,
                                            "plastic":30.0})
        electrode_circut_board = sba_recipe("Electrode Circut Board",
                                            builder = "Assemblers",
                                            rate = 5,
                                            inputs = {"rubber":30.0,
                                                      "petrolium coke":45.0})
        silicon_circut_board = sba_recipe("Silicon Circut Board",
                                          builder = "Assemblers",
                                          rate = 12.5,
                                          inputs = {"copper sheet":27.5,
                                                    "silica":27.5})
        caterium_circut_board = sba_recipe("Caterium Circut Board",
                                           builder = "Assemblers",
                                           rate = 8.75,
                                           inputs = {"plastic":12.5,
                                                     "quickwire":37.5})

        if "electode circut board" in self.alternate_recipes:
            self.recipes["circut board"] = electrode_circut_board
        elif "silicon circut board" in self.alternate_recipes:
            self.recipes["circut board"] = silicon_circut_board
        elif "caterium circut board" in self.alternate_recipes:
            self.recipes["circut board"] = caterium_circut_board
        else:
            self.recipes["circut board"] = circut_board


        #adaptive control unit
        adaptive_control_unit = sba_recipe("Adaptive Control Unit",
                                           builder = "Manufacturers",
                                           rate = 1.0,
                                           inputs = {"automated wiring":7.5,
                                                     "circut board":5.0,
                                                     "heavy modular frame":1.0,
                                                     "computer":1.0})

        self.recipes["adaptive control unit"] = adaptive_control_unit


        #turbo rifle ammo
        turbo_rifle_ammo = sba_recipe ("Turbo Rifle Ammo",
                                       builder = "Blenders",
                                       rate = 250.0,
                                       inputs = {"rifle ammo":125,
                                                 "aluminum casing":15.0,
                                                 "turbofuel":15.0})

        self.recipes["turbo rifle ammo"] = turbo_rifle_ammo


        #homing rifle ammo
        homing_rifle_ammo = sba_recipe("Homing Rifle Ammo",
                                       builder = "Assemblers",
                                       rate = 25.0,
                                       inputs = {"rifle ammo":50.0,
                                                "high-speed connector":2.5})

        self.recipes["homing rifle ammo"] = homing_rifle_ammo


        #explosive rebar
        explosive_rebar = sba_recipe("Explosive Rebar",
                                     builder = "Manufacturers",
                                     rate = 5.0,
                                     inputs = {"iron rebar":10.0,
                                               "smokeless powder":10.0,
                                               "steel pipe":10.0})

        self.recipes["explosive rebar"] = explosive_rebar


        #iron rebar
        iron_rebar = sba_recipe("Iron Rebar",
                                builder = "Constructors",
                                rate = 15.0,
                                inputs = {"iron rod":15.0})

        self.recipes["iron rebar"] = iron_rebar


        #shatter rebar
        shatter_rebar = sba_recipe("Shatter Rebar",
                                builder = "Assemblers",
                                rate = 5.0,
                                inputs = {"iron rebar":10.0,
                                         "quartz crystal":15.0})

        self.recipes["shatter rebar"] = shatter_rebar


        #stun rebar
        stun_rebar = sba_recipe("Stun Rebar",
                                   builder = "Assemblers",
                                   rate = 10.0,
                                   inputs = {"iron rebar":10.0,
                                             "quickwire":50.0})

        self.recipes["stun rebar"] = stun_rebar


        #nuke nobelisk
        nuke_nobelisk = sba_recipe("Nuke Nobelisk",
                                   builder = "Manufacturers",
                                   rate = 0.5,
                                   inputs = {"nobelisk":2.5,
                                             "encased uranium cell":10.0,
                                             "smokeless powder":5.0,
                                             "ai limiter":3.0})

        self.recipes["nuke nobelisk"] = nuke_nobelisk


        #cluster nobelisk
        cluster_nobelisk = sba_recipe("Cluster Nobelisk",
                                      builder = "Assemblers",
                                      rate = 2.5,
                                      inputs = {"nobelisk":7.5,
                                                "smokeless powder":10.0})

        self.recipes["cluster nobelisk"] = cluster_nobelisk


        #pulse nobelisk
        pulse_nobelisk = sba_recipe("Pulse Nobelisk",
                                    builder = "Assemblers",
                                    rate = 5.0,
                                    inputs = {"nobelisk":5.0,
                                              "crystal oscillator":1.0})

        self.recipes["pulse nobelisk"] = pulse_nobelisk


        #nobelisk
        nobelisk = sba_recipe("Nobelisk",
                              builder = "Assemblers",
                              rate = 10.0,
                              inputs = {"steel pipe":20.0,
                                        "black powder":20.0})

        self.recipes["nobelisk"] = nobelisk


        #iodine infused filter
        iodine_infused_filter = sba_recipe("Iodine Infused Filter",
                                           builder = "Manufacturers",
                                           rate = 3.75,
                                           inputs = {"gas filter":3.75,
                                                     "quickwire":30.0,
                                                     "aluminum casing":3.75})

        self.recipes["iodine infused filter"] = iodine_infused_filter


        #gas filter
        gas_filter = sba_recipe("Gas Filter",
                                builder = "Manufacturers",
                                rate = 7.5,
                                inputs = {"coal":37.5,
                                         "rubber":15,
                                         "fabric":15.0})

        self.recipes["gas filter"] = gas_filter


        #beacon
        beacon = sba_recipe("Beacon",
                            builder = "Manufacturers",
                            rate = 7.5,
                            inputs = {"iron plate":22.5,
                                     "iron rod":7.5,
                                     "wire":112.5,
                                     "cable":15.0})
        crystal_beacon = sba_recipe("Crystal Beacon",
                                    builder = "Manufacturers",
                                    rate = 10.0,
                                    inputs = {"steel beam":2.0,
                                             "steel pipe":8.0,
                                             "crystal oscillator":0.5})

        self.recipes["beacon"] = crystal_beacon if "crystal beacon" in self.alternate_recipes else beacon


        #packaged turbofuel
        packaged_turbofuel = sba_recipe("Packaged Turbofuel",
                                        builder = "Packagers",
                                        rate = 20.0,
                                        inputs = {"turbofuel":20.0,
                                                  "empty canister":20.0})

        self.recipes["packaged turbofuel"] = packaged_turbofuel


        #turbofuel
        turbofuel = sba_recipe("Turbofuel",
                               builder = "Refineries",
                               rate = 18.75,
                               inputs = {"fuel":22.5,
                                         "compacted coal":15.0})
        turbo_heavy_fuel = sba_recipe("Turbo Heavy Fuel",
                                      builder = "Refineries",
                                      rate = 30.0,
                                      inputs = {"heavy oil residue":37.5,
                                                "compacted coal":30.0})
        turbo_blend_fuel = sba_recipe("Turbo Blend Fuel",
                                      builder = "Blenders",
                                      rate = 45.0,
                                      inputs = {"fuel":15.0,
                                                "heavy oil residue":30.0,
                                                "sulfur":22.5,
                                                "petrolium coke":22.5})

        if "turbo heavy fuel" in self.alternate_recipes:
            self.recipes["turbofuel"] = turbo_heavy_fuel
        elif "turbo blend fuel" in self.alternate_recipes:
            self.recipes["turbofuel"] = turbo_blend_fuel
        else:
            self.recipes["turbofuel"] = turbofuel


        #supercomputer
        supercomputer = sba_recipe("Supercomputer",
                                   builder = "Manufacturers",
                                   rate = 1.875,
                                   inputs = {"computer":3.75,
                                             "ai limiter":3.75,
                                             "high-speed connector":5.625,
                                             "plastic":52.5})
        oc_supercomputer = sba_recipe("OC Supercomputer",
                                      builder = "Assemblers",
                                      rate  = 3.0,
                                      inputs = {"radio control unit":9.0,
                                                "cooling system":9.0})
        super_state_computer = sba_recipe("Super State Computer",
                                          builder = "Manufacturers",
                                          rate = 2.4,
                                          inputs = {"computer":3.6,
                                                    "electromagnetic control rod":2.5,
                                                    "battery":24.0,
                                                    "wire":54.0})
        if "oc supercomputer" in self.alternate_recipes:
            self.recipes["supercomputer"] = oc_supercomputer
        elif "super state computer" in self.alternate_recipes:
            self.recipes["supercomputer"] = super_state_computer
        else:
            self.recipes["supercomputer"] = supercomputer


        #quickwire
        quickwire = sba_recipe("Quickwire",
                               builder = "Constructors",
                               rate = 60.0,
                               inputs = {"caterium ingot":12.0})
        fused_quickwire = sba_recipe("Fused Quickwire",
                                     builder = "Assembler",
                                     rate = 90.0,
                                     inputs = {"caterium ingot":7.5,
                                               "copper ingot":37.5})

        self.recipes["quickwire"] = fused_quickwire if "fused quickwire" in self.alternate_recipes else quickwire


        #quartz crystal
        quartz_crystal = sba_recipe("Quartz Crystal",
                                    builder = "Constructors",
                                    rate = 22.5,
                                    inputs = {"raw quartz":37.5})
        pure_quartz_crystal = sba_recipe("Pure Quartz Crystal",
                                         builder = "Refineries",
                                         rate = 52.5,
                                         inputs = {"raw quartz":67.5,
                                                   "water":37.5})

        self.recipes["quartz crystal"] = pure_quartz_crystal if "pure quartz crystal" in self.alternate_recipes else quartz_crystal


        #silica
        silica = sba_recipe("Silica",
                            builder = "Constructors",
                            rate = 37.5,
                            inputs = {"raw quartz":22.5})
        cheap_silica = sba_recipe("Cheap Silica",
                                  builder = "Assembler",
                                  rate = 26.5,
                                  inputs = {"raw quartz":11.25,
                                            "limestone":18.75})

        self.recipes["silica"] = cheap_silica if "cheap silica" in self.alternate_recipes else silica


        #smokeless powder
        smokeless_powder = sba_recipe("Smokeless Powder",
                                      builder = "Refineries",
                                      rate = 20.0,
                                      inputs = {"black powder":20.0,
                                                "heavy oil residue":10.0})

        self.recipes["smokeless powder"] = smokeless_powder


        #high speed connector
        high_speed_connector = sba_recipe("High-Speed Connector",
                                          builder = "Manufacturers",
                                          rate = 3.75,
                                          inputs = {"quickwire":210.0,
                                                    "cable":37.5,
                                                    "circut board":3.75})
        silicon_high_speed_connector = sba_recipe("Silicon High-Speed Connector",
                                                  builder = "Manufacturers",
                                                  rate = 3.0,
                                                  inputs = {"quickwire":90.0,
                                                            "silica":37.5,
                                                            "circut board":3.0})

        self.recipes["high-speed connector"] = silicon_high_speed_connector if "silicon high-speed connector" in self.alternate_recipes else high_speed_connector


        #fabric
        polyester_fabric = sba_recipe("Polyester Fabric",
                                      builder = "Refineries",
                                      rate = 30.0,
                                      inputs = {"polymer resin":30.0,
                                                "water":30.0})

        self.recipes["fabric"] = polyester_fabric


        #crystal oscillator
        crystal_oscillator = sba_recipe("Crystal Oscillator",
                                        builder = "Manufacturers",
                                        rate = 1.0,
                                        inputs = {"quartz crystal":18.0,
                                                  "cable":14.0,
                                                  "reinforced iron plate":2.5})
        insulated_crystal_oscillator = sba_recipe("Insulated Crystal Oscillator",
                                                  builder = "Manufacturers",
                                                  rate = 1.875,
                                                  inputs = {"quartz crystal":18.75,
                                                            "rubber":13.125,
                                                            "ai limiter":1.875})

        self.recipes["crystal oscillator"] = insulated_crystal_oscillator if "insulated crystal oscillator" in self.alternate_recipes else crystal_oscillator


        #compacted Coal
        compacted_coal = sba_recipe("Compacted Coal",
                                    builder = "Assembler",
                                    rate = 25.0,
                                    inputs = {"coal":25.0,
                                              "sulfur":25.0})

        self.recipes["compacted coal"] = compacted_coal


        #caterium ingot
        caterium_ingot = sba_recipe("Caterium Ingot",
                                    builder = "Smelters",
                                    rate = 15.0,
                                    inputs = {"caterium ore":45.0})
        pure_caterium_ingot = sba_recipe("Pure Caterium Ingot",
                                         builder = "Refineries",
                                         rate = 12.0,
                                         inputs = {"caterium ore":24.0,
                                                   "water":24.0})

        self.recipes["caterium ingot"] = pure_caterium_ingot if "pure caterium ingot" in self.alternate_recipes else caterium_ingot


        #black powder
        black_powder = sba_recipe("Black Powder",
                                  builder = "Assemblers",
                                  rate = 30.0,
                                  inputs = {"coal":15.0,
                                            "sulfur":15.0})
        fine_black_powder = sba_recipe("Fine Black Powder",
                                       builder = "Assembler",
                                       rate = 15.0,
                                       inputs = {"sulfur":7.5,
                                                 "compacted coal":3.75})

        self.recipes["black powder"] = fine_black_powder if "fine black powder" in self.alternate_recipes else black_powder


        #AI limiter
        ai_limiter = sba_recipe("AI Limiter",
                                builder = "Assemblers",
                                rate = 5.0,
                                inputs = {"copper sheet":25.0,
                                          "quickwire":100.0})

        self.recipes["ai limiter"] = ai_limiter


        #uranium waste
        uranium_waste = sba_recipe("Uranium Waste",
                                   builder = "Nuclear Power Plants",
                                   rate = 10.0,
                                   inputs = {"uranium fuel rod":0.2,
                                             "water":240.0})

        self.recipes["uranium waste"] = uranium_waste


        #thermal propulsion rocket
        thermal_propulsion_rocket = sba_recipe("Thermal Propulsion Rocket",
                                               builder = "Manufacturers",
                                               rate = 1.0,
                                               inputs = {"modular engine":2.5,
                                                         "turbo motor":1.0,
                                                         "cooling system":3.0,
                                                         "fused modular frame":1.0})

        self.recipes["thermal propulsion rocket"] = thermal_propulsion_rocket


        #turbo motor
        turbo_motor = sba_recipe("Turbo Motor",
                                 builder = "Manufacturers",
                                 rate = 1.875,
                                 inputs = {"cooling system":7.5,
                                           "radio control unit":3.75,
                                           "motor":7.5,
                                           "rubber":45.0})
        turbo_electric_motor = sba_recipe("Turbo Electric Motor",
                                          builder = "Manufacturers",
                                          rate = 2.8125,
                                          inputs = {"motor":6.5625,
                                                    "radio control unit":8.4375,
                                                    "electromagnetic control rod":4.6875,
                                                    "rotor":6.5625})
        turbo_pressure_motor = sba_recipe("Turbo Pressure Motor",
                                          builder = "Manufacturers",
                                          rate = 3.75,
                                          inputs = {"motor":7.5,
                                                    "pressure conversion cube":1.875,
                                                    "packaged nitrogen gas":45.0,
                                                    "stator":15.0})

        if "turbo electric motor" in self.alternate_recipes:
            self.recipes["turbo motor"] = turbo_electric_motor
        elif "turbo pressure motor" in self.alternate_recipes:
            self.recipes["turbo motor"] = turbo_pressure_motor
        else:
            self.recipes["turbo motor"] = turbo_motor


        #uranium fuel rod
        uranium_fuel_rod = sba_recipe("Uranium Fuel Rod",
                                      builder = "Manufacturers",
                                      rate = 0.4,
                                      inputs = {"encased uranium cell":20.0,
                                                "encased industrial beam":1.2,
                                                "electromagnetic control rod":5.0})
        uranium_fuel_unit = sba_recipe("Uranium Fuel Unit",
                                       builder = "Manufacturers",
                                       rate = 0.6,
                                       inputs = {"encased uranium cell":20.0,
                                                 "electromagnetic control rod":2.0,
                                                 "crystal oscillator":0.6,
                                                 "beacon":1.2})

        self.recipes["uranium fuel rod"] = uranium_fuel_unit if "uranium fuel unit" in self.alternate_recipes else uranium_fuel_rod


        #pressure conversion cube
        pressure_conversion_cube = sba_recipe("Pressure Conversion Cube",
                                              builder = "Assembler",
                                              rate = 1.0,
                                              inputs = {"fused modular frame":1.0,
                                                        "radio control unit":2.0})

        self.recipes["pressure conversion cube"] = pressure_conversion_cube


        #plutonium waste
        plutonium_waste = sba_recipe("Plutonium Waste",
                                     builder = "Nuclear Power Plants",
                                     rate = 1.0,
                                     inputs = {"plutonium fuel rod":0.1,
                                               "water":240.0})

        self.recipes["plutonium waste"] = plutonium_waste


        #plutonium pellet
        plutonium_pellet = sba_recipe("Plutonium Pellet",
                                      builder = "Particle Accelerators",
                                      rate = 30.0,
                                      inputs = {"non-fissile uranium":100.0,
                                                "uranium waste":25.0})

        self.recipes["plutonium pellet"] = plutonium_pellet


        #packaged nitric acid
        packaged_nitric_acid = sba_recipe("Packaged Nitric Acid",
                                          builder = "Packagers",
                                          rate = 30.0,
                                          inputs = {"nitric acid":30.0,
                                                   "empty fluid tank":30.0})

        self.recipes["packaged nitric acid"]= packaged_nitric_acid


        #non fissle uranium
        non_fissile_uranium = sba_recipe("Non-fissile Uranium",
                                         builder = "Blenders",
                                         rate = 50.0,
                                         inputs = {"uranium waste":37.5,
                                                   "silica":25.0,
                                                   "nitric acid":15.0,
                                                   "sulfuric acid":15.0},
                                         byproducts = {"water":15.0})
        fertile_uranium = sba_recipe("Fertile Uranium",
                                     builder = "Blenders",
                                     rate = 100.0,
                                     inputs = {"uranium":25.0,
                                               "uranium waste":25.0,
                                               "nitric acid":15.0,
                                               "sulfuric acid":25.0},
                                     byproducts = {"water":40.0})

        self.recipes["non-fissile uranium"] = fertile_uranium if "fertile uranium" in self.alternate_recipes else non_fissile_uranium


        #nuclear pasta
        nuclear_pasta = sba_recipe("Nuclear Pasta",
                                   builder = "Particle Accelerators",
                                   rate = 0.5,
                                   inputs = {"copper powder":100.0,
                                             "pressure conversion cube":0.5})

        self.recipes["nuclear pasta"] = nuclear_pasta


        #plutonium fuel Rod
        plutonium_fuel_rod = sba_recipe("Plutonium Fuel Rod",
                                        builder = "Manufacturers",
                                        rate = 0.25,
                                        inputs = {"encased plutonium cell":7.5,
                                                  "steel beam":4.5,
                                                  "electromagnetic control rod":1.5,
                                                  "heat sink":2.5})
        plutonium_fuel_unit = sba_recipe("Plutonium Fuel Unit",
                                         builder = "Assembler",
                                         rate = 0.5,
                                         inputs = {"encased plutonium cell":10.0,
                                                   "pressure conversion cube":0.5})

        self.recipes["plutonium fuel rod"] = plutonium_fuel_unit if "plutonium fuel unit" in self.alternate_recipes else plutonium_fuel_rod


        #nitric acid
        nitric_acid = sba_recipe("Nitric Acid",
                                 builder = "Blenders",
                                 rate = 30.0,
                                 inputs = {"nitrogen gas":120.0,
                                           "water":30.0,
                                           "iron plate":10.0})

        self.recipes["nitric acid"] = nitric_acid


        #magnetic field generator
        magnetic_field_generator = sba_recipe("Magnetic Field Generator",
                                              builder = "Manufacturers",
                                              rate = 1.0,
                                              inputs = {"versatile framework":2.5,
                                                        "electromagnetic control rod":1.0,
                                                        "battery":5.0})

        self.recipes["magnetic field generator"] = magnetic_field_generator


        #heat sink
        heat_sink = sba_recipe("Heat Sink",
                               builder = "Assemblers",
                               rate = 7.5,
                               inputs = {"alclad aluminum sheet":37.5,
                                         "copper sheet":22.5})
        heat_exchanger = sba_recipe("Heat Exchanger",
                                    builder = "Assemblers",
                                    rate = 10.0,
                                    inputs = {"aluminum casing":30.0,
                                              "rubber":30.0})

        self.recipes["heat sink"] = heat_exchanger if "heat exhanger" in self.alternate_recipes else heat_sink


        #fused modular frame
        fused_modular_frame = sba_recipe("Fused Modular Frame",
                                      builder = "Blenders",
                                      rate = 1.5,
                                      inputs = {"heavy modular frame":1.5,
                                                "aluminum casing":75.0,
                                                "nitrogen gas":37.5})
        heat_fused_frame = sba_recipe("Heat-Fused Frame",
                                      builder = "Blenders",
                                      rate = 3.0,
                                      inputs = {"heavy modular frame":3.0,
                                                "aluminum ingot":150.0,
                                                "nitric acid":24.0,
                                                "fuel":30.0})

        self.recipes["fused modular frame"] = heat_fused_frame if "heat fused frame" in self.alternate_recipes else fused_modular_frame


        #encased uranium cell
        encased_uranium_cell = sba_recipe("Encased Uranium Cell",
                                          builder = "Blenders",
                                          rate = 25.0,
                                          inputs = {"uranium":50.0,
                                                    "concrete":15.0,
                                                    "sulfuric acid":40.0},
                                          byproducts = {"sulfuric acid":10.0})
        infused_uranium_cell = sba_recipe("Infused Uranium Cell",
                                          builder = "Manufacturers",
                                          rate = 20.0,
                                          inputs = {"uranium":25.0,
                                                    "silica":25.0,
                                                    "sulfur":25.0,
                                                    "quickwire":75.0})

        self.recipes["encased uranium cell"] = infused_uranium_cell if "infused uranium cell" in self.alternate_recipes else encased_uranium_cell


        #encased plutonium cell
        encased_plutonium_cell = sba_recipe("Encased Plutonium Cell",
                                            builder = "Assemblers",
                                            rate = 5.0,
                                            inputs = {"plutonium pellet":10.0,
                                                      "concrete":20.0})
        instant_plutonium_cell = sba_recipe("Instant Plutonium Cell",
                                            builder = "Particle Accelerators",
                                            rate = 10.0,
                                            inputs = {"non-fissile uranium":75.0,
                                                      "aluminum casing":10.0})

        self.recipes["encased plutonium cell"] = instant_plutonium_cell if "instant plutonium cell" in self.alternate_recipes else encased_plutonium_cell


        #empty fluid tank
        empty_fluid_tank = sba_recipe("Empty Fluid Tank",
                                      builder = "Constructors",
                                      rate = 60.0,
                                      inputs = {"aluminum ingot":60.0})

        self.recipes["empty fluid tank"] = empty_fluid_tank


        #electromagnetic control rod
        electromagnetic_control_rod = sba_recipe("Electromagnetic Control Rod",
                                                 builder = "Assemblers",
                                                 rate = 4.0,
                                                 inputs = {"stator":6.0,
                                                           "ai limiter": 4.0})
        electromagnetic_connection_rod = sba_recipe("Electromagnetic Connection Rod",
                                                    builder = "Assemblers",
                                                    rate = 8.0,
                                                    inputs = {"stator":8.0,
                                                              "high-speed connector":4.0})

        self.recipes["electromagnetic control rod"] = electromagnetic_connection_rod if "electromagnetic connection rod" in self.alternate_recipes else electromagnetic_control_rod


        #copper powder
        copper_powder = sba_recipe("Copper Powder",
                                   builder = "Constructors",
                                   rate = 50.0,
                                   inputs = {"copper ingot":300.0})

        self.recipes["copper powder"]= copper_powder


        #cooling system
        cooling_system = sba_recipe("Cooling System",
                                    builder = "Blenders",
                                    rate = 6.0,
                                    inputs = {"heat sink":12.0,
                                              "rubber":12.0,
                                              "water":30.0,
                                              "nitrogen gas":150.0})
        cooling_device = sba_recipe("Cooling Device",
                                    builder = "Blenders",
                                    rate = 3.75,
                                    inputs = {"heat sink":9.375,
                                              "motor":1.875,
                                              "nitrogen gas":45.0})

        self.recipes["cooling system"] = cooling_device if "cooling device" in self.alternate_recipes else cooling_system


    def add_product(self, product, rate):

        # Add the final product to the products list
        if product.lower() in self.products:
            self.products[product.lower()] += rate
        else:
            self.products[product.lower()] = rate

        # resolve the full recipe
        self.resolve_recipe(product.lower(), rate)

    def resolve_recipe(self, product, rate, from_recipe=None):

        #check if the nformationn is there. I probably forgot or have not slogged through the full list yet.
        if product not in self.recipes:
            print("Whoopsies! Looks like you spelled ", product," wrong or Jacob forgot to add the product information.")
            if from_recipe is not None:
                print("Or, more likely, Jacob misspelled the product details...")
                print("Check the product info for:", from_recipe)
            quit()

        # Get the item information
        product_info = self.recipes[product]

        # check if it is a resource or set stop point and add it to the resources list if so
        if product_info.is_resource:
            if product in self.resources or product in self.stop_points:
                self.resources[product] += rate
            else:
                self.resources[product] = rate

        else:
            # if it's not a resource, add it to the intermediates and resolve each of it's ingredients
            multiplier = rate/product_info.rate

            #add the item to the list of things we are making
            if product in self.intermediates:
                self.intermediates[product] += rate
            else:
                self.intermediates[product] = rate

            # Check if this produces any byproducts and add them
            for key, value in product_info.byproducts.items():
                if key in self.byproducts:
                    self.byproducts[key] += value*multiplier
                else:
                    self.byproducts[key] = value*multiplier
            # Now resolve each of the ingredients
            for key, value in product_info.inputs.items():
                self.resolve_recipe(key, value*multiplier, product_info.name)

    def print_result(self):
        print("In order to produce")
        for key, value in self.products.items():
            print(value, " ", key)
        print("")
        print("you will need to construct")
        for key, value in self.intermediates.items():
            print(math.ceil(value/self.recipes[key].rate), 
                  self.recipes[key].builder, "for", 
                  value, 
                  self.recipes[key].name)
        print("")
        print("and provide the following resources")
        for key, value in self.resources.items():
            print(value, key)
        print("")
        print("You will have to handle the following byproducts.")
        for key, value in self.byproducts.items():
            print(value, key)

def main():
    my_recipe = sba_product_list()
    my_recipe.add_product("smart plating", 2)
    my_recipe.add_product("Assembly Director System",5)
    my_recipe.print_result()

if __name__ == "__main__":
    main()
