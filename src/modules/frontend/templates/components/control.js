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
        soket: "192.168.1.101:5000",
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