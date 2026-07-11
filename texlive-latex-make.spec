%global tl_name latex-make
%global tl_revision 79369

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.4.4
Release:	%{tl_revision}.1
Summary:	Easy compiling of complex (and simple) LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/latex-make
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-make.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-make.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-make.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides several tools that aim to simplify the compilation
of LaTeX documents: LaTeX.mk: a Makefile snippet to help compiling LaTeX
documents in DVI, PDF, PS, ... format. Dependencies are automatically
tracked: one should be able to compile documents with a one-line
Makefile containing include LaTeX.mk. Complex documents (with multiple
bibliographies, indexes, glossaries, ...) should be correctly managed.
figlatex.sty: a LaTeX package to easily insert xfig figures (with
\includegraphics{file.fig}). It can interact with LaTeX.mk so that the
latter automatically invokes transfig if needed. And various helper
tools for LaTeX.mk. This package requires GNUmake (>= 3.81).

