import streamlit as st
import io
from gfpgan import GFPGANer
import numpy as np
from PIL import Image

@st.cache_resource
def load_model():
    # Carga el modelo GFPGAN (se descarga automáticamente desde GitHub)
    model = GFPGANer(
        model_path='https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth',
        upscale=1,  # Sin upscale para mayor rapidez
        arch='clean',
        channel_multiplier=2
    )
    return model

def main():
    st.title("🖼️ Restauración Facial Rápida con GFPGAN")
    st.markdown("Sube una imagen y restaura los rostros automáticamente usando IA local.")

    uploaded_file = st.file_uploader("Selecciona una imagen", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)

        if st.button("Restaurar Rostros"):
            with st.spinner("Procesando... Esto puede tomar 5-15 segundos."):
                model = load_model()
                img_np = np.array(image)
                # Procesar con GFPGAN
                _, _, restored_img = model.enhance(img_np, has_aligned=False, only_center_face=False, paste_back=True)
                restored_pil = Image.fromarray(restored_img)

            st.success("¡Restauración completada!")

            # Mostrar en paralelo
            col1, col2 = st.columns(2)

            with col1:
                st.image(image, caption="Imagen Original", use_column_width=True)
                st.write(f"**Dimensiones:** {image.size[0]} x {image.size[1]}")
                # Tamaño en bytes
                buf_orig = io.BytesIO()
                image.save(buf_orig, format="PNG")
                st.write(f"**Tamaño:** {len(buf_orig.getvalue())} bytes")

            with col2:
                st.image(restored_pil, caption="Imagen Restaurada", use_column_width=True)
                st.write(f"**Dimensiones:** {restored_pil.size[0]} x {restored_pil.size[1]}")
                # Tamaño en bytes
                buf_rest = io.BytesIO()
                restored_pil.save(buf_rest, format="PNG")
                st.write(f"**Tamaño:** {len(buf_rest.getvalue())} bytes")

            # Opción de descarga
            buf = io.BytesIO()
            restored_pil.save(buf, format="PNG")
            buf.seek(0)
            st.download_button(
                label="Descargar Imagen Restaurada",
                data=buf,
                file_name="imagen_restaurada.png",
                mime="image/png",
                key="download"
            )
        else:
            st.image(image, caption="Imagen Original", use_column_width=True)

if __name__ == "__main__":
    main()