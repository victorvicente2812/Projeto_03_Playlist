import streamlit as st 

generos = {
    'Trap' : {
        'Matuê' : 'https://www.youtube.com/watch?v=aq-DH4iwviE',
        'Alee' : 'https://www.youtube.com/watch?v=s1EApaujb04'
    },
    'Funk' : {
        'Mc Kevin' : 'https://www.youtube.com/watch?v=WciF0b4OTgE',
        'Mc IG' : 'https://www.youtube.com/watch?v=2_ZFQkl6MPc'
    },
    'Pagode' : {
        'Zeca Pagodinho' : 'https://www.youtube.com/watch?v=oTREAvZbmME',
        'Tiaguinho' : 'https://www.youtube.com/watch?v=qUqc_cYejX0'
    },
    'Eletronica' : {
        'Alok' : 'https://www.youtube.com/watch?v=JVpTp8IHdEg',
        'Calvin Harris' : 'https://www.youtube.com/watch?v=ebXbLfLACGM'
    }
}

st.sidebar.title('VT🥷')
st.sidebar.image('logo.png')

genero = st.sidebar.selectbox('Selecionar um genero musical', generos.keys())
artista = st.sidebar.selectbox('Selecione um atista', generos[genero].keys())

st.title(artista)
video, sobre = st.tabs(['Video', 'Sobre o artista'])

with video:
    st.video(generos[genero][artista])

with sobre:
    if artista == 'matuê':
        st.markdown('''
            Matheus Brasileiro Aguiar (Nasceu em 11/10/1993, Fortaleza-CE), Conhecido como um dos maiores nomes do trap brasileiro, é fundador da gravadora 30PRAUM.
                    ''')
    elif artista == 'Alee':
        st.write('''
            Alisson Vieira Silva (Nasceu em 30/08/2001, Salvador-BH), conhecido por suas músicas de trap e melodias marcantes, ganhou destaque rapidamente na cena do trap nacional.
                 ''')
    elif artista == 'Mc Kevin':
        st.write('''
            kevin Nascimento Bueno (Nasceu em 29/04/1998, São Paulo-SP), conhecido por seus sucessos no funk, começou a cantar ainda adolecente
                 ''')
    elif artista == 'Mc IG':
        st.write('''
                 Gabriel Ferreira (Nasceu em 09/10/1998, São Paulo-SP), conhecido pelo funk de rua e estilo único, é um dos artistas mais ouvidos de gênero atualmente
                 ''')
    elif artista == 'Zeca Pagodinho':
        st.write('''
                 Jessé Gomes da Silva Filho (Nasceu em 04/02/1959, Rio de Janeiro-RJ), conhecido como ícone do samba, foi descoberto pela cantora Beth Carvalho
                 ''')
    elif artista == 'Tiaguinho':
        st.write('''
                 Thiago André Barbosa (Nasceu em 11/03/1983, Presidente Prudente-SP), conhecido pelo pagode, fez parte do grupo exaltasamba
                 ''')
    elif artista == 'Alok':
        st.write('''
                 Alok Achkar Peres Petrillo (nasceu em 26/08/1991, Goiânia-GO), conhecido como DJ internacional, seus pais também são DJs
                 ''')
    elif artista == 'Calvin Harris':
        st.write('''
                 Adam Richard Wiles (Nasceu em 17/01/1994, Escócia), conhecido por seu hits de música eletronica, já ganhou vários prêmios internacionais
                 ''')