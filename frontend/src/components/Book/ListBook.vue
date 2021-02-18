<template>
   <div class="container">
        <div class="row">
            <div class="col text-left">
                <div>
                    <h2 class="mb-4">Listado de Libros</h2>
                    <b-button size="sm" :to="{name: 'NewBook'}" variant="info">
                        Nuevo Libro
                    </b-button>
                </div>
                <br><br>
                <div class="col-md-12 text-center">
                    <b-table striped hover :items="books" :fields="fields">
                        <template #cell(action)="data">
                            <b-button size="sm" variant="primary" :to="{name: 'EditBook', params: { BookId: data.item.id}}">
                                Editar
                            </b-button>
                            <b-button size="sm" variant="danger" :to="{name: 'DeleteBook', params: { BookId: data.item.id}}">
                                Eliminar
                            </b-button>
                        </template>

                    </b-table>
                    
                </div>
            </div>
        </div>

    </div> 
</template>

<script>

import axios from 'axios';

export default {
  
    data () {
        return {
            fields: [
                {key: 'title', label: 'Título'},
                {key: 'description', label: 'Descripción'},
                {key: 'action', label: 'Acción'},
                
            ],
            books: []
        }
    },
    methods: {

        getBooks() {

            const path = 'http://localhost:8000/api/v1.0/books/';
            axios.get(path).then(response => {

                this.books = response.data
            })
            .catch( error => {

                console.log(error)

            })
        }
    },
    created() {

        this.getBooks()
    }
  
}
</script>