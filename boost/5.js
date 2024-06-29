const attributeTypeMap={
    "product":"Product",
    "orderId":"String",
    "sku":"String",
    "title":"String",
    "price":"Int"
}
class File {
    #type;
    #attribute;
    #color;
    #label;
    #num;
    #attributeTypeMap;
    
    constructor(type_arr, attribute_arr, attributeTypeMap, num, color, label) {
        this.#type = type_arr;
        this.#attribute = attribute_arr;
        this.#attributeTypeMap = attributeTypeMap;
        this.#color = color;
        this.#label = label;
        this.#num = num;
    }
    
    printGraph() {
        console.log(`   subgraph cluster_${this.#num} {`);
        for (let i = 0; i < this.#type.length; i++) {
            console.log(`       ${this.#type[i]} [shape=box style=filled color=cyan];`);
        }
        for (let i = 0; i < this.#attribute.length; i++) {
            console.log(`       ${this.#attribute[i]};`);
        }
        console.log(`       label = "${this.#label}.file";`);
        console.log(`       color = ${this.#color};\n   }`);
    }
    
    printRelations() {
        let relations = "";
        for (let i = 0; i < this.#attribute.length; i++) {
            const attribute = this.#attribute[i];
            const type = this.#attributeTypeMap[attribute];
            relations += `    ${attribute} -> ${type};\n`;
        }
        return relations;
    }
}

class Packages {
    #label;
    #files;
    
    constructor(name, files) {
        this.#label = name;
        this.#files = files;
    }
    
    printGraph() {
        console.log(`   subgraph cluster_${this.#label === "Service" ? '0' : '9'} {`);
        console.log(`       style = tab;`);
        console.log(`       color = blue;`);
        console.log(`       label = "${this.#label} Package";`);
        this.#files.forEach((file) => {
            file.printGraph();
        });
        console.log("   }");
    }
    
    printRelations() {
        let relations = "";
        this.#files.forEach((file) => {
            relations += file.printRelations();
        });
        return relations;
    }
}

const Packages_name = {
    Service: [
        new File(["Product"], ["sku", "price", "title"], attributeTypeMap, 1, "lightgrey", "Product"),
        new File(["Order"], ["orderId", "product"],attributeTypeMap, 2, "lightgrey", "Order")
    ],
    System: [
        new File(["String", "Int"], [], {}, 10, "lightgrey", "Source")
    ]
};
function main() {
    const readline = require('readline');
    
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question('어떤 패키지를 호출하겠는가? : ', (answer) => {
        if (Packages_name[answer]) {
            const packageFiles = Packages_name[answer];
            const custom_package = new Packages(answer, packageFiles);
            const system_package = new Packages("System", Packages_name["System"]);


            console.log(`digraph G {`);
            custom_package.printGraph();
            system_package.printGraph();
            console.log(custom_package.printRelations());
            console.log(system_package.printRelations());
            console.log(`}`);
            console.log(`${answer} Package를 그리겠습니다.`);
        } else {
            console.log("존재하지 않는 패키지입니다.");
        }
        rl.close();
    });
}

main();
