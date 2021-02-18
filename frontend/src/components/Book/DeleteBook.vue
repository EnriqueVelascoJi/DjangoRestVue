<template>
   <div class="container">
        <div class="row">
            <div class="col">

                <h3>¿Estas seguro eliminar este libro?</h3>
                <p>Título : {{ this.element.title }}</p>
                <p>Descripción : {{ this.element.description }}</p>

            </div>
        </div>

        <div class="row">
            <div class="col">

                <b-button v-on:click="deleteBook" variant="danger">
                    Eliminar libro
                </b-button>
            </div>
        </div>

    </div> 
</template>

<script>

import axios from 'axios';
import Swal from 'sweetalert2'


export default {
  

  data() {

    return {
        bookId: this.$route.params.BookId,
        element: {
            title: '',
            description: ''
        }
    }
  },
  methods: {

      getBook() {

        const path = `http://localhost:8000/api/v1.0/books/${this.bookId}/`;

        axios.get(path).then( resp => {

            this.element.title = resp.data.title;
            this.element.description = resp.data.description;
        })
        .catch( error => {
            console.log(error);
        })
      },
      deleteBook() {

        const path = `http://localhost:8000/api/v1.0/books/${this.bookId}/`;

        axios.delete(path).then( resp => {

            location.href = '/books';
        })
        .catch( error => {
            
            Swal.fire({
                icon: 'error',
                title: 'Error ',
                text: 'Algo salió mal, vuelve a intentar',
              })
        })

      }
  },
  created() {

      this.getBook();
  }
  
}
</script>