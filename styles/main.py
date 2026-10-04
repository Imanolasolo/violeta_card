"""
Estilos globales de la tarjeta.
"""

import streamlit as st


def load_styles():

    st.markdown(
        """
        <style>

        /* =================================================
           RESET / STREAMLIT
           ================================================= */

        #MainMenu {
            visibility: hidden;
        }

        header {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        [data-testid="stSidebar"] {
            display: none;
        }

        .block-container {
            max-width: 760px;
            padding-top: 1rem;
            padding-bottom: 2rem;
        }


        /* =================================================
           BODY
           ================================================= */

        .stApp {
            background: #ffffff;
        }


        /* =================================================
           TARJETA PRINCIPAL
           ================================================= */

        .digital-card {
            background: #ffffff;
            border-radius: 28px;
            padding: 28px;
            margin: 10px auto;
            max-width: 680px;
        }


        /* =================================================
           BRAND
           ================================================= */

        .brand {
            display: flex;
            justify-content: flex-start;
            align-items: center;
            margin-bottom: 25px;
        }

        .brand-logo {
            max-width: 180px;
            max-height: 80px;
            object-fit: contain;
        }


        /* =================================================
           HERO
           ================================================= */

        .hero {
            text-align: center;
            margin-bottom: 30px;
        }

        .profile-photo {
            width: 140px;
            height: 140px;
            border-radius: 50%;
            object-fit: cover;
            margin-bottom: 18px;
        }

        .profile-photo-placeholder {
            width: 140px;
            height: 140px;
            border-radius: 50%;
            margin: 0 auto 18px auto;

            display: flex;
            align-items: center;
            justify-content: center;

            background: #eeeeee;
            font-size: 32px;
            font-weight: 600;
        }

        .hero h1 {
            font-size: 32px;
            margin: 0;
            font-weight: 700;
            color: #1b1b1b;
        }

        .role {
            margin-top: 8px;
            font-size: 18px;
            font-weight: 600;
        }

        .organization {
            margin-top: 4px;
            font-size: 15px;
            color: #666666;
        }

        .quote {
            margin: 22px auto 0 auto;
            max-width: 500px;
            font-size: 16px;
            font-style: italic;
            color: #555555;
            line-height: 1.6;
        }


        /* =================================================
           ACTIONS
           ================================================= */

        .actions {
            display: grid;
            grid-template-columns:
                repeat(3, 1fr);

            gap: 10px;
            margin-bottom: 14px;
        }

        .action-button {
            display: flex;
            align-items: center;
            justify-content: center;

            padding: 13px 10px;

            border-radius: 12px;
            border: 1px solid #dddddd;

            text-decoration: none !important;

            color: #222222 !important;
            font-weight: 600;
            font-size: 14px;

            transition: 0.2s ease;
        }

        .action-button:hover {
            transform: translateY(-2px);
            border-color: #999999;
        }

        .action-button.primary {
            background: #222222;
            color: white !important;
            border-color: #222222;
        }


        /* =================================================
           SECTIONS
           ================================================= */

        .content-section {
            border-top: 1px solid #eeeeee;
            padding-top: 24px;
            margin-top: 28px;
        }

        .content-section h2 {
            font-size: 20px;
            margin-bottom: 10px;
        }

        .content-section p {
            color: #555555;
            line-height: 1.7;
            font-size: 15px;
        }


        /* =================================================
           FOOTER
           ================================================= */

        .card-footer {
            border-top: 1px solid #eeeeee;
            margin-top: 32px;
            padding-top: 20px;
            text-align: center;
        }

        .location {
            font-size: 14px;
            color: #666666;
            margin-bottom: 14px;
        }

        .social-links {
            display: flex;
            justify-content: center;
            gap: 18px;
            margin-bottom: 20px;
        }

        .social-links a {
            color: #555555 !important;
            text-decoration: none !important;
            font-size: 13px;
        }

        .footer-brand {
            font-size: 12px;
            color: #999999;
        }


        /* =================================================
           MOBILE
           ================================================= */

        @media (max-width: 600px) {

            .block-container {
                padding: 0.5rem;
            }

            .digital-card {
                padding: 22px 18px;
                border-radius: 20px;
            }

            .hero h1 {
                font-size: 27px;
            }

            .actions {
                grid-template-columns: 1fr;
            }

        }

        </style>
        """,
        unsafe_allow_html=True,
    )