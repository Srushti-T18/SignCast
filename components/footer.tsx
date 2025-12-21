import { Hand } from "lucide-react"

export function Footer() {
  return (
    <footer className="bg-muted/50 border-t border-border/60 py-16">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-12 mb-12">
          <div className="md:col-span-1">
            <div className="flex items-center gap-3 mb-5">
              <div className="flex items-center justify-center w-11 h-11 rounded-xl bg-gradient-to-br from-primary to-secondary shadow-md">
                <Hand className="w-6 h-6 text-primary-foreground" aria-hidden="true" />
              </div>
              <span className="text-xl font-semibold tracking-tight text-foreground">SignCast</span>
            </div>
            <p className="text-sm text-muted-foreground leading-relaxed">
              Breaking communication barriers with AI-powered sign language translation.
            </p>
          </div>

          <div>
            <h3 className="font-semibold text-foreground mb-5">Product</h3>
            <ul className="space-y-3.5">
              <li>
                <a href="#" className="text-sm text-muted-foreground hover:text-accent transition-colors duration-200">
                  Features
                </a>
              </li>
              <li>
                <a href="#" className="text-sm text-muted-foreground hover:text-accent transition-colors duration-200">
                  Pricing
                </a>
              </li>
              <li>
                <a href="#" className="text-sm text-muted-foreground hover:text-accent transition-colors duration-200">
                  Demo
                </a>
              </li>
              <li>
                <a href="#" className="text-sm text-muted-foreground hover:text-accent transition-colors duration-200">
                  API
                </a>
              </li>
            </ul>
          </div>

          <div>
            <h3 className="font-semibold text-foreground mb-5">Company</h3>
            <ul className="space-y-3.5">
              <li>
                <a href="#" className="text-sm text-muted-foreground hover:text-accent transition-colors duration-200">
                  About
                </a>
              </li>
              <li>
                <a href="#" className="text-sm text-muted-foreground hover:text-accent transition-colors duration-200">
                  Blog
                </a>
              </li>
              <li>
                <a href="#" className="text-sm text-muted-foreground hover:text-accent transition-colors duration-200">
                  Careers
                </a>
              </li>
              <li>
                <a href="#" className="text-sm text-muted-foreground hover:text-accent transition-colors duration-200">
                  Contact
                </a>
              </li>
            </ul>
          </div>

          <div>
            <h3 className="font-semibold text-foreground mb-5">Resources</h3>
            <ul className="space-y-3.5">
              <li>
                <a href="#" className="text-sm text-muted-foreground hover:text-accent transition-colors duration-200">
                  Documentation
                </a>
              </li>
              <li>
                <a href="#" className="text-sm text-muted-foreground hover:text-accent transition-colors duration-200">
                  Support
                </a>
              </li>
              <li>
                <a href="#" className="text-sm text-muted-foreground hover:text-accent transition-colors duration-200">
                  Privacy
                </a>
              </li>
              <li>
                <a href="#" className="text-sm text-muted-foreground hover:text-accent transition-colors duration-200">
                  Terms
                </a>
              </li>
            </ul>
          </div>
        </div>

        <div className="pt-10 border-t border-border/60">
          <p className="text-sm text-muted-foreground text-center">
            © {new Date().getFullYear()} SignCast. All rights reserved. Building accessible technology for everyone.
          </p>
        </div>
      </div>
    </footer>
  )
}
