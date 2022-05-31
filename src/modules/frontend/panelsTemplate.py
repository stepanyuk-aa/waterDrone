def gen_control_panel(backend_soket):
    text = """
app.component("control-panel", {
  template: 
    /*html*/
    `
    <div id="txt_1" >
            <div class="triggers">
                <div class="table">
                    <p><b>Режим:</b> Стоп</p>
                </div>
                <div class="table">
                    <p><b>Координаты: </b>ш.{{triggers["coordinates"][0]}}, д.{{triggers["coordinates"][1]}}</p>, 
                </div>
                <div class="table">
                    <p><b>Скорость: </b>{{triggers["speed"]}}</p>
                </div>
                <div class="table">
                    <p><b>Дальномер: </b> {{triggers["usr"]}} см </p>
                </div> 
            </div>   
            <div class="main">

                <div class="buttons">
                    <div class="left">
                        <input class="button" onclick="to_left()" type="button" value="⬅">
                    </div>
                    <div class="center">
                        <input class="button" onclick="to_direct()" type="button" value="⬆">
                        <input class="button" onclick="to_stop()" type="button" value="🛑">
                    </div>
                    <div class="right">
                        <input class="button" onclick="to_right()" type="button" value="➡">
                    </div>
                </div>
                <div class="speed">
                    <input class="button" onclick="set_speed(2000)" type="button" value="2000">
                    <input class="button" onclick="set_speed(1800)" type="button" value="1800">
                    <input class="button" onclick="set_speed(1600)" type="button" value="1600">
                    <input class="button" onclick="set_speed(1400)" type="button" value="1400">
                    <input class="button" onclick="set_speed(1200)" type="button" value="1200">
                    <input class="button" onclick="set_speed(1000)" type="button" value="1000">
                    <input class="button" onclick="set_speed(0)" type="button" value="0">
                </div>
             </div>

        </div>
    `,
  data() {
    return {
"""
    text += f'soket: "{backend_socket}",'
    text += """
        triggers: {
            "coordinates": [0,0],
            "speed": 0,
            "usr":0
        }
    }
  },
  mounted() {
    axios
      .get("http://" + this.soket + "/get/triggers")
      .then(response => (this.triggers = response.data))
      .catch(error => console.log(error));
  }
})
"""
    return text

def gen_script_panel(backend_soket):
    text = """
app.component("scripts-panel", {
  template: 
    /*html*/
    `
    <div id="txt_2" >
            <div class="panel_scripts">
                <div class="buttons_scripts">
                    <input class="button2" type="button" v-on:click="new_script" value="Новый сценарий">
                    <input class="button2" type="button" v-on:click="save_script" value="Сохранить">
                    <input class="button2" type="button" v-on:click="run_script" value="Запуск">
                    <input class="button2" type="button" v-on:click="edit_script" value="Редактировать">
                </div>
                <div v-show="active_new_script" class="new_script">
                    <label>Название: </label>
                    <input type="text" v-model="select_script_title">
                    <label> .py </label>
                    <input type="button" v-on:click="close_script" value="Отмена">
                    <input type="button" v-on:click="add_script" value="Добавить">
                    <input type="button" v-on:click="delite_script" value="Удалить">
                </div>
                
                <div class="script_column">
                    <div class="scripts">
                        <input v-for="text, file in scripts_data" :key="file" type="button"  v-model="file" v-on:click="select_script(file)">
                    </div>
                    <div class="editor" contenteditable="false" v-model="select_script_text" ref="editor" @input="editEditor">
                        
                    </div>
                </div> 
                <div class="logs">
                  <textarea class=logs-textarea readonly disabled rows=6 ref="logs">{{script_output}}</textarea>
                </div>                    
            </div>
        </div>
    `,
  data() {
    return {
"""
    text += f'soket: "{backend_socket}",'
    text += """
        script_header: `# Base Header
        #######################################
        import config
        from modules.modules import modules
        from drivers.drivers import drivers
        
        drivers = drivers()
        modules = modules(drivers, config)
        #######################################
        `,
        allow_edit: false,
        active_new_script: false,
        select_script_title: "",
        select_script_text: "",
        script_output: undefined,
        scripts_data: {
        },
    }
  },
  methods: {
    new_script: function (event) {
        this.close_script();
        this.active_new_script = !this.active_new_script;
        this.select_script_text = this.script_header;
        this.$refs.editor.innerText = this.select_script_text;
    },

    edit_script: function (event) {
      this.allow_edit = !this.allow_edit;
      this.$refs.editor.setAttribute("contentEditable", this.allow_edit);
  },
    
    save_script: function (event) {
        file = this.select_script_title + ".py";
        this.scripts_data[file] = this.select_script_text;

        axios.post("http://" + this.soket + "/create/script", {
          title: this.select_script_title,
          text: this.select_script_text,
        })
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        });
    },

	  delite_script: function (event) {
        file = this.select_script_title + ".py"
        if (this.scripts_data[file]){
          delete this.scripts_data[file];
        }

        axios.post("http://" + this.soket + "/delite/script", {
          title: this.select_script_title,
        })
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        });

        this.close_script();
    },

    add_script: function (event) {
        file = this.select_script_title;
        if (!this.select_script_title.includes(".py")){
          file = this.select_script_title + ".py";
        }
        if (!this.scripts_data[file]){
          this.scripts_data[file] = "";
        }
    },
    
	  close_script() {
        this.active_new_script = false;
        this.select_script_title = "";
        this.select_script_text = "";
        this.$refs.editor.innerText = "";
	  },
	  select_script(file) {
        this.select_script_title = file.replace(".py","");
            // this.get_script_data(this.select_script_title);
            
        this.select_script_text = this.scripts_data[file];
        this.$refs.editor.innerText = this.scripts_data[file];
            
        this.active_new_script = true;
        this.$refs.editor.setAttribute("contentEditable", false);
    },

    run_script: function (event) {
      file = this.select_script_title + ".py"
      this.script_output = "Wait..."
      var vm = this;

      axios.post("http://" + this.soket + "/run/script", {
        title: file,
      })
      .then(function (response) {
        vm.script_output = response.data;
        console.log(vm.script_output);
      })
      .catch(function (error) {
        console.log(error);
      })
      .catch(function (error) {
        console.log(error);
      }); 
      
  },

    // refs
    /////////////////////////////////////////////////////////////////
    editEditor(e) {
        this.select_script_text = e.target.innerText;
        file = this.select_script_title + ".py"
        this.scripts_data[file] = this.select_script_text;
    },
    // get_script_data(file){
    //     data = "";
    //     axios.post("http://" + this.soket + "/get/script/data", {
    //         title: file,
    //     })
    //     .then(response => (this.scripts_data[file] = response.data))
    //     .catch(function (error) {
    //         console.log(error);
    //     });
    // },
  },
  mounted() {
    axios
      .get("http://" + this.soket + "/get/scripts")
      .then(response => (this.scripts_data = response.data))
      .catch(error => console.log(error));
  }
})
"""
    return text