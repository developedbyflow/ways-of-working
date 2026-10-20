/*
 * <Product>: the C4 model (https://c4model.com), one source for every C4 drawing of the design.
 * Structurizr DSL (https://docs.structurizr.com/dsl); drawn by ../diagrams.sh, views listed in views.txt.
 * One relationship per direction; each label starts with its row number in the table under the drawing.
 * Filled in by /system-design (context, containers, data), /architecture (components).
 */
workspace "<Product>" "The design's C4 model." {

    !identifiers hierarchical
    !impliedRelationships false

    model {
        user = person "<Role>" "<What they do.>"
        product = softwareSystem "<Product>" "<What it does, in one sentence.>" {
            app = container "App" "<What it does.>" "<Technology>"
            api = container "API" "<What it does.>" "<Technology>"
            database = container "Database" "<What it holds.>" "<Technology>" "Database"
        }
        outside = softwareSystem "<Outside system>" "<What it does for us.>" "External"

        user -> product "1. <What the person does with it>"
        product -> outside "2. <What goes, what comes back>" "<HTTPS>"

        user -> product.app "1. <Uses the app>"
        product.app -> product.api "2. <Data requests>" "HTTPS"
        product.api -> product.database "3. Reads and writes" "SQL"
        product.api -> outside "4. <What goes>" "<HTTPS>"
    }

    views {
        systemContext product "context" {
            title "<Product> – C4 level 1: system context"
            include *
            autoLayout lr
        }
        container product "containers" {
            title "<Product> – C4 level 2: containers"
            include *
            autoLayout lr
        }

        properties {
            "c4plantuml.tags" "true"
            "c4plantuml.legend" "false"
        }

        styles {
            element "Person" {
                shape Person
                background #08427b
                color #ffffff
            }
            element "Software System" {
                background #1168bd
                color #ffffff
            }
            element "Container" {
                background #438dd5
                color #ffffff
            }
            element "Component" {
                background #85bbf0
                color #000000
            }
            element "Library" {
                background #cfe3f7
                color #000000
                border dashed
            }
            element "External" {
                background #999999
                color #ffffff
            }
            element "Database" {
                shape Cylinder
            }
            element "Health data" {
                stroke #c0392b
                strokeWidth 4
            }
            relationship "Relationship" {
                style solid
            }
            relationship "Import" {
                style dashed
            }
        }
    }
}
