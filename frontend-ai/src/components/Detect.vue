<template>
  <v-container fluid>
    <v-row justify="center">
      <v-col cols="12" md="6">
        <v-card outlined rounded="lg">
          <v-card-title class="text-h4 justify-center">
            Detección de imágenes
          </v-card-title>
          <v-card-text>
            <v-row justify-md="space-around" align="center">
              <v-col cols="12" md="4">
                <v-file-input
                  label="Cargar imágen"
                  v-model="img"
                  @change="onFileChange"
                ></v-file-input>
              </v-col>

              <v-col cols="12" md="4">
                <v-card outlined v-if="url">
                  <v-card-text>
                    <v-img max-width="200" max-height="300" :src="url" />
                  </v-card-text>
                </v-card>
                <v-card
                  outlined
                  v-else
                  width="400"
                  height="250"
                  class="d-flex justify-center align-center"
                >
                  <v-card-text class="text-center">
                    Esperando imágen...
                  </v-card-text>
                </v-card>
              </v-col>
            </v-row>
          </v-card-text>
          <v-card-actions>
            <v-btn block color="indigo" @click="uploadImg">detectar</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col cols="12" md="3">
        <v-card outlined rounded="lg" v-if="detect">
          <v-card-title class="text-h5 justify-center">
            Tu imagen es:
          </v-card-title>
          <v-card-text class="text-center text-h3">:v {{ detect }}</v-card-text>
        </v-card>
        <v-card v-else>
          <v-card-title> Esperando a detectar algo... :v </v-card-title>
        </v-card>
      </v-col>
    </v-row>
    <!-- Notificaciones -->
    <v-snackbar
      v-model="snackbar"
      :timeout="1400"
      :color="notify.color"
      centered
      multi-line
      elevation="24"
    >
      {{ notify.text }}
      <template v-slot:action="{ attrs }">
        <v-btn dark text v-bind="attrs" @click="snackbar = false" icon>
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </template>
    </v-snackbar>
  </v-container>
</template>

<script>
import axios from "axios";
const url = "http://localhost:4000";

export default {
  data() {
    return {
      //resultado del api
      detect: null,
      //preview del imagen
      url: null,
      // imagen a subir
      img: null,
      // notificaciones
      snackbar: false,
      notify: { text: null, color: null },
    };
  },
  methods: {
    async uploadImg() {
      try {
        const img = this.img;
        let formData = new FormData();
        formData.append("file", img);
        const response = await axios.post(`${url}/img`, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        });
        this.detect = response.data.detect;
        this.notify.text = response.data.message;
        this.notify.color = "success";
        this.snackbar = true;
      } catch (error) {
        this.notify.text = "Error!";
        this.notify.color = "error";
        this.snackbar = true;
        console.error(error);
      }
    },

    onFileChange(e) {
      const file = e;
      if (file) {
        this.url = URL.createObjectURL(file);
        URL.revokeObjectURL(file);
      } else {
        this.url = null;
      }
    },
  },
};
</script>

<style></style>
