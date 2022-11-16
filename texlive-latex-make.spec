Name:		texlive-latex-make
Version:	60874
Release:	1
Summary:	Easy compiling of complex (and simple) LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/latex-make
License:	gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-make.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-make.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-make.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides several tools that aim to simplify the
compilation of LaTeX documents: LaTeX.mk: a Makefile snippet to
help compiling LaTeX documents in DVI, PDF, PS, ... format.
Dependencies are automatically tracked: one should be able to
compile documents with a one-line Makefile containing 'include
LaTeX.mk'. Complex documents (with multiple bibliographies,
indexes, glossaries, ...) should be correctly managed.
figlatex.sty: a LaTeX package to easily insert xfig figures
(with \includegraphics{file.fig}). It can interact with
LaTeX.mk so that the latter automatically invokes transfig if
needed. And various helper tools for LaTeX.mk This package
requires GNUmake (>= 3.81).

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/support/latex-make
%{_texmfdistdir}/tex/latex/latex-make
%{_texmfdistdir}/scripts/latex-make
%doc %{_texmfdistdir}/doc/support/latex-make

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
