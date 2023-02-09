import Link from "next/link";

export default function RootLayout({ children }) {

    return (
        <html>
            <body>
                <div>
                    <Link href={'/'}>Root</Link> <br />
                    <Link href={'/home'}>Home</Link> <br />
                    <Link href={'/admin'}>Admin</Link>
                </div>
                {children}
            </body>
        </html>
    )
}
