import Vue from "vue";
import Vuetify from "vuetify/lib/framework";

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        themes: {
            light: {
                primary: "#85DB46",
                secondary: "#375C1D",
                accent: "#AFE1BC",
                error: "#b71c1c",
            },
        },
        options: {
            customProperties: true,
        },
    },
});
